#first load all the packages
library(adegenet)
library(ape)
library(hierfstat)
library(pegas)
library(tidyverse)
library(qqman)

#set the working directory
setwd("/Users/eamoncorbett/Desktop/THESIS/FINAL_SNP_datasets/Final_Genepops/")

#load the genepop file
default_gen <- read.genepop("genepop_f_M4n4_r60.gen", ncode=3L)

#some basic checking on that genepop
nLoc(default_gen)
pop(default_gen)
gensum_default<- summary(default_gen)
gensum_default
plot(genSum$X) #can use this to explore the summary stats

#now we set up some color schemes
myCol <- c("purple","red","magenta","green","yellow","black","gray") #includes outgroups, also works for all P. rufifrons
southernCol<- c("purple","magenta","green","yellow") #works for just southern rufifrons
BlendCol<- c("purple","yellow","green","yellow") #works for just southern rufifrons without differentiating rufifrons and specularis
nospecCol<- c("purple","green","yellow") #works for just southern rufifrons or just peru/chaco
testCol<- c("#800000","#008080","#C0C0C0","#000080")
newCol<-c("#F19E4E", "#CB1C23","#9CD1E4", "#2466A6")


#and now subset the dataset to include or not include various populations
all_rufifrons <- default_gen[pop=c("MZUSP_MA135_rufispec","AMNH_DOT_8874_inornatus","UF_49269_peru","MZUSP_P11_rufispec","MZUSP_FSK192_sincipitalis")]
southern_rufifrons <- default_gen[pop=c("MZUSP_MA135_rufispec","UF_49269_peru","MZUSP_P11_rufispec","MZUSP_FSK192_sincipitalis")]
southern_rufifrons_no_spec <- default_gen[pop=c("UF_49269_peru","MZUSP_P11_rufispec","MZUSP_FSK192_sincipitalis")]
peru_chaco <- default_gen[pop=c("UF_49269_peru","MZUSP_FSK192_sincipitalis")]
peru_nominate <- default_gen[pop=c("UF_49269_peru","MZUSP_P11_rufispec")]
chaco_nominate <- default_gen[pop=c("MZUSP_FSK192_sincipitalis","MZUSP_P11_rufispec")]

#k means clustering
grp <- find.clusters(southern_rufifrons, max.n.clust=10)
table(pop(southern_rufifrons), grp$grp)

#PCA for all individuals
x<-scaleGen(default_gen,NA.method="mean")
pca_all<-dudi.pca(x, scale=FALSE)
s.class(pca_all$li, as.factor(pop(default_gen)),xax=1,yax=2, col=myCol,grid=F,cstar=0,axesell=F,cpoint=2,label=NULL,cellipse=F)

#PCA for all P. rufifrons
y<-scaleGen(all_rufifrons,NA.method="mean")
pca_rufifrons<-dudi.pca(y, scale=FALSE)
s.class(pca_rufifrons$li, as.factor(pop(all_rufifrons)),xax=1,yax=2, col=myCol,grid=F,cstar=0,axesell=F,cpoint=2,label=NULL,cellipse=F)

#PCA for all Southern P. rufifrons
z<-scaleGen(southern_rufifrons,NA.method="mean")
pca_southern<-dudi.pca(z, scale=FALSE)
s.class(pca_southern$li, as.factor(pop(southern_rufifrons)),xax=1,yax=2, col=newCol,grid=F,cstar=0,axesell=F,cpoint=2,label=NULL,cellipse=F)

#NJ phylogeny of all individuals
all_dist <- dist(tab(default_gen))
all_tree <- nj(all_dist)
plot(all_tree,type="unrooted")
write.nexus(all_tree, file="default_tree_all.nex")

#NJ phylogeny of all P. rufifrons
rufifrons_dist <- dist(tab(all_rufifrons))
rufifrons_tree <- nj(rufifrons_dist)
plot(rufifrons_tree,type="unrooted")
write.nexus(rufifrons_tree, file="default_tree_rufifrons.nex")

#NJ phylogeny of southern P. rufifrons
southern_dist <- dist(tab(southern_rufifrons))
southern_tree <- nj(southern_dist)
plot(southern_tree,type="unrooted")
write.nexus(southern_tree, file="default_tree_southern.nex")

