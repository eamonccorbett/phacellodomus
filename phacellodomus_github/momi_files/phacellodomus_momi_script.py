#ok so in this script we're going to do 10 different single-direction pulse migrations of .1
#25 repeats of each, which will take a pretty long time
#then going to pick the best 2, do a model with both of them, etc etc

#the basic setup stuff
source activate momi-py36
cd Desktop/THESIS/momi
python
import momi

sfs = momi.Sfs.load("sfs1.gz")

#model 1 is going to be peruvianus to sincipitalis
migration_r1m1= momi.DemographicModel(N_e=2.5e5)
migration_r1m1.set_data(sfs)
#pop size parameters
migration_r1m1.add_size_param("n_peruvianus")
migration_r1m1.add_size_param("n_sincipitalis")
migration_r1m1.add_size_param("n_rufifrons")
migration_r1m1.add_size_param("n_specularis")
#migration time parameter
migration_r1m1.add_time_param("tm")
#make the tree, with pop size parameters when we add leaves
migration_r1m1.add_leaf("peruvianus", N="n_peruvianus")
migration_r1m1.add_leaf("sincipitalis", N="n_sincipitalis")
migration_r1m1.add_leaf("rufifrons", N= "n_rufifrons")
migration_r1m1.add_leaf("specularis", N="n_specularis")
#split time parameters. tm is the first event to happen
migration_r1m1.add_time_param("t1", lower_constraints=["tm"])
migration_r1m1.add_time_param("t2", lower_constraints=["t1"])
migration_r1m1.add_time_param("t3", lower_constraints=["t2"])
#the actual splitting events
migration_r1m1.move_lineages("peruvianus", "sincipitalis", t="t1")
migration_r1m1.move_lineages("sincipitalis", "rufifrons", t="t2")
migration_r1m1.move_lineages("rufifrons", "specularis", t="t3")
#the single migration event
migration_r1m1.move_lineages("peruvianus", "sincipitalis", t="tm", p=0.1)
#not doing the one test run because that adds a lot of time
#migration_r1m1.optimize(method="L-BFGS-B")
#set up for 25 runs
results_r1m1 = []
n_runs = 25
#do the 25 runs
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    migration_r1m1.set_params(randomize=True)
    results_r1m1.append(migration_r1m1.optimize(method="L-BFGS-B", options={"maxiter":200}))
# sort results according to log likelihood, pick the best (largest) one
best_result_r1m1 = sorted(results_r1m1, key=lambda r: r.log_likelihood)[-1]
migration_r1m1.set_params(best_result_r1m1.parameters)
best_result_r1m1
#calculate the AIC
import numpy as np
for model in [migration_r1m1]:
    lik = model.log_likelihood()
    nparams = len(model.get_params())
    aic = 2*nparams - 2*lik
    print("AIC {}".format(aic))


#model 2 is going to be sincipitalis to peruvianus
migration_r1m2= momi.DemographicModel(N_e=2.5e5)
migration_r1m2.set_data(sfs)
#pop size parameters
migration_r1m2.add_size_param("n_peruvianus")
migration_r1m2.add_size_param("n_sincipitalis")
migration_r1m2.add_size_param("n_rufifrons")
migration_r1m2.add_size_param("n_specularis")
#migration time parameter
migration_r1m2.add_time_param("tm")
#make the tree, with pop size parameters when we add leaves
migration_r1m2.add_leaf("peruvianus", N="n_peruvianus")
migration_r1m2.add_leaf("sincipitalis", N="n_sincipitalis")
migration_r1m2.add_leaf("rufifrons", N= "n_rufifrons")
migration_r1m2.add_leaf("specularis", N="n_specularis")
#split time parameters. tm is the first event to happen
migration_r1m2.add_time_param("t1", lower_constraints=["tm"])
migration_r1m2.add_time_param("t2", lower_constraints=["t1"])
migration_r1m2.add_time_param("t3", lower_constraints=["t2"])
#the actual splitting events
migration_r1m2.move_lineages("peruvianus", "sincipitalis", t="t1")
migration_r1m2.move_lineages("sincipitalis", "rufifrons", t="t2")
migration_r1m2.move_lineages("rufifrons", "specularis", t="t3")
#the single migration event
migration_r1m2.move_lineages("sincipitalis", "peruvianus", t="tm", p=0.1)
#not doing the one test run because that adds time
#migration_r1m2.optimize(method="L-BFGS-B")
#set up for 25 runs
results_r1m2 = []
n_runs = 25
#do the 25 runs
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    migration_r1m2.set_params(randomize=True)
    results_r1m2.append(migration_r1m2.optimize(method="L-BFGS-B", options={"maxiter":200}))
# sort results according to log likelihood, pick the best (largest) one
best_result_r1m2 = sorted(results_r1m2, key=lambda r: r.log_likelihood)[-1]
migration_r1m2.set_params(best_result_r1m2.parameters)
best_result_r1m2
#calculate the AIC
import numpy as np
for model in [migration_r1m2]:
    lik = model.log_likelihood()
    nparams = len(model.get_params())
    aic = 2*nparams - 2*lik
    print("AIC {}".format(aic))

#model 3 is going to be sincipitalis to rufifrons
migration_r1m3= momi.DemographicModel(N_e=2.5e5)
migration_r1m3.set_data(sfs)
#pop size parameters
migration_r1m3.add_size_param("n_peruvianus")
migration_r1m3.add_size_param("n_sincipitalis")
migration_r1m3.add_size_param("n_rufifrons")
migration_r1m3.add_size_param("n_specularis")
#migration time parameter
migration_r1m3.add_time_param("tm")
#make the tree, with pop size parameters when we add leaves
migration_r1m3.add_leaf("peruvianus", N="n_peruvianus")
migration_r1m3.add_leaf("sincipitalis", N="n_sincipitalis")
migration_r1m3.add_leaf("rufifrons", N= "n_rufifrons")
migration_r1m3.add_leaf("specularis", N="n_specularis")
#split time parameters. tm is the first event to happen
migration_r1m3.add_time_param("t1", lower_constraints=["tm"])
migration_r1m3.add_time_param("t2", lower_constraints=["t1"])
migration_r1m3.add_time_param("t3", lower_constraints=["t2"])
#the actual splitting events
migration_r1m3.move_lineages("peruvianus", "sincipitalis", t="t1")
migration_r1m3.move_lineages("sincipitalis", "rufifrons", t="t2")
migration_r1m3.move_lineages("rufifrons", "specularis", t="t3")
#the single migration event
migration_r1m3.move_lineages("sincipitalis", "rufifrons", t="tm", p=0.1)
#not doing the one test run because that adds time
#migration_r1m3.optimize(method="L-BFGS-B")
#set up for 25 runs
results_r1m3 = []
n_runs = 25
#do the 25 runs
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    migration_r1m3.set_params(randomize=True)
    results_r1m3.append(migration_r1m3.optimize(method="L-BFGS-B", options={"maxiter":200}))
# sort results according to log likelihood, pick the best (largest) one
best_result_r1m3 = sorted(results_r1m3, key=lambda r: r.log_likelihood)[-1]
migration_r1m3.set_params(best_result_r1m3.parameters)
best_result_r1m3
#calculate the AIC
import numpy as np
for model in [migration_r1m3]:
    lik = model.log_likelihood()
    nparams = len(model.get_params())
    aic = 2*nparams - 2*lik
    print("AIC {}".format(aic))

#model 4 is going to be rufifrons to sincipitalis
migration_r1m4= momi.DemographicModel(N_e=2.5e5)
migration_r1m4.set_data(sfs)
#pop size parameters
migration_r1m4.add_size_param("n_peruvianus")
migration_r1m4.add_size_param("n_sincipitalis")
migration_r1m4.add_size_param("n_rufifrons")
migration_r1m4.add_size_param("n_specularis")
#migration time parameter
migration_r1m4.add_time_param("tm")
#make the tree, with pop size parameters when we add leaves
migration_r1m4.add_leaf("peruvianus", N="n_peruvianus")
migration_r1m4.add_leaf("sincipitalis", N="n_sincipitalis")
migration_r1m4.add_leaf("rufifrons", N= "n_rufifrons")
migration_r1m4.add_leaf("specularis", N="n_specularis")
#split time parameters. tm is the first event to happen
migration_r1m4.add_time_param("t1", lower_constraints=["tm"])
migration_r1m4.add_time_param("t2", lower_constraints=["t1"])
migration_r1m4.add_time_param("t3", lower_constraints=["t2"])
#the actual splitting events
migration_r1m4.move_lineages("peruvianus", "sincipitalis", t="t1")
migration_r1m4.move_lineages("sincipitalis", "rufifrons", t="t2")
migration_r1m4.move_lineages("rufifrons", "specularis", t="t3")
#the single migration event
migration_r1m4.move_lineages("rufifrons", "sincipitalis", t="tm", p=0.1)
#not doing the one test run because that adds time
#migration_r1m4.optimize(method="L-BFGS-B")
#set up for 25 runs
results_r1m4 = []
n_runs = 25
#do the 25 runs
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    migration_r1m4.set_params(randomize=True)
    results_r1m4.append(migration_r1m4.optimize(method="L-BFGS-B", options={"maxiter":200}))
# sort results according to log likelihood, pick the best (largest) one
best_result_r1m4 = sorted(results_r1m4, key=lambda r: r.log_likelihood)[-1]
migration_r1m4.set_params(best_result_r1m4.parameters)
best_result_r1m4
#calculate the AIC
import numpy as np
for model in [migration_r1m4]:
    lik = model.log_likelihood()
    nparams = len(model.get_params())
    aic = 2*nparams - 2*lik
    print("AIC {}".format(aic))

#model 5 is going to be rufifrons to specularis
migration_r1m5= momi.DemographicModel(N_e=2.5e5)
migration_r1m5.set_data(sfs)
#pop size parameters
migration_r1m5.add_size_param("n_peruvianus")
migration_r1m5.add_size_param("n_sincipitalis")
migration_r1m5.add_size_param("n_rufifrons")
migration_r1m5.add_size_param("n_specularis")
#migration time parameter
migration_r1m5.add_time_param("tm")
#make the tree, with pop size parameters when we add leaves
migration_r1m5.add_leaf("peruvianus", N="n_peruvianus")
migration_r1m5.add_leaf("sincipitalis", N="n_sincipitalis")
migration_r1m5.add_leaf("rufifrons", N= "n_rufifrons")
migration_r1m5.add_leaf("specularis", N="n_specularis")
#split time parameters. tm has to happen before t2 but not necessarily before t1
migration_r1m5.add_time_param("t1")
migration_r1m5.add_time_param("t2", lower_constraints=["t1", "tm"])
migration_r1m5.add_time_param("t3", lower_constraints=["t2"])
#the actual splitting events
migration_r1m5.move_lineages("peruvianus", "sincipitalis", t="t1")
migration_r1m5.move_lineages("sincipitalis", "rufifrons", t="t2")
migration_r1m5.move_lineages("rufifrons", "specularis", t="t3")
#the single migration event
migration_r1m5.move_lineages("rufifrons", "specularis", t="tm", p=0.1)
#not doing the one test run because that adds time
#migration_r1m5.optimize(method="L-BFGS-B")
#set up for 25 runs
results_r1m5 = []
n_runs = 25
#do the 25 runs
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    migration_r1m5.set_params(randomize=True)
    results_r1m5.append(migration_r1m5.optimize(method="L-BFGS-B", options={"maxiter":200}))
# sort results according to log likelihood, pick the best (largest) one
best_result_r1m5 = sorted(results_r1m5, key=lambda r: r.log_likelihood)[-1]
migration_r1m5.set_params(best_result_r1m5.parameters)
best_result_r1m5
#calculate the AIC
import numpy as np
for model in [migration_r1m5]:
    lik = model.log_likelihood()
    nparams = len(model.get_params())
    aic = 2*nparams - 2*lik
    print("AIC {}".format(aic))

#model 6 is going to be specularis to rufifrons
migration_r1m6= momi.DemographicModel(N_e=2.5e5)
migration_r1m6.set_data(sfs)
#pop size parameters
migration_r1m6.add_size_param("n_peruvianus")
migration_r1m6.add_size_param("n_sincipitalis")
migration_r1m6.add_size_param("n_rufifrons")
migration_r1m6.add_size_param("n_specularis")
#migration time parameter
migration_r1m6.add_time_param("tm")
#make the tree, with pop size parameters when we add leaves
migration_r1m6.add_leaf("peruvianus", N="n_peruvianus")
migration_r1m6.add_leaf("sincipitalis", N="n_sincipitalis")
migration_r1m6.add_leaf("rufifrons", N= "n_rufifrons")
migration_r1m6.add_leaf("specularis", N="n_specularis")
#split time parameters. tm has to happen before t2 but not necessarily before t1
migration_r1m6.add_time_param("t1")
migration_r1m6.add_time_param("t2", lower_constraints=["t1", "tm"])
migration_r1m6.add_time_param("t3", lower_constraints=["t2"])
#the actual splitting events
migration_r1m6.move_lineages("peruvianus", "sincipitalis", t="t1")
migration_r1m6.move_lineages("sincipitalis", "rufifrons", t="t2")
migration_r1m6.move_lineages("rufifrons", "specularis", t="t3")
#the single migration event
migration_r1m6.move_lineages("specularis", "rufifrons", t="tm", p=0.1)
#not doing the one test run because that adds time
#migration_r1m6.optimize(method="L-BFGS-B")
#set up for 25 runs
results_r1m6 = []
n_runs = 25
#do the 25 runs
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    migration_r1m6.set_params(randomize=True)
    results_r1m6.append(migration_r1m6.optimize(method="L-BFGS-B", options={"maxiter":200}))
# sort results according to log likelihood, pick the best (largest) one
best_result_r1m6 = sorted(results_r1m6, key=lambda r: r.log_likelihood)[-1]
migration_r1m6.set_params(best_result_r1m6.parameters)
best_result_r1m6
#calculate the AIC
import numpy as np
for model in [migration_r1m6]:
    lik = model.log_likelihood()
    nparams = len(model.get_params())
    aic = 2*nparams - 2*lik
    print("AIC {}".format(aic))

#these are the no migration models


#population sizes are fixed within populations but different between populations-- null model
popsize_r0_m0 = momi.DemographicModel(N_e=2.5e5)
popsize_r0_m0.set_data(sfs)
#pop size parameters
popsize_r0_m0.add_size_param("n_peruvianus")
popsize_r0_m0.add_size_param("n_sincipitalis")
popsize_r0_m0.add_size_param("n_rufifrons")
popsize_r0_m0.add_size_param("n_specularis")
#make the tree, with pop size parameters when we add leaves
popsize_r0_m0.add_time_param("t1")
popsize_r0_m0.add_leaf("peruvianus", N="n_peruvianus")
popsize_r0_m0.add_leaf("sincipitalis", N="n_sincipitalis")
popsize_r0_m0.move_lineages("peruvianus", "sincipitalis", t="t1")
popsize_r0_m0.add_leaf("rufifrons", N= "n_rufifrons")
popsize_r0_m0.add_time_param("t2", lower_constraints=["t1"])
popsize_r0_m0.move_lineages("sincipitalis", "rufifrons", t="t2")
popsize_r0_m0.add_leaf("specularis", N="n_specularis")
popsize_r0_m0.add_time_param("t3", lower_constraints=["t2"])
popsize_r0_m0.move_lineages("rufifrons", "specularis", t="t3")
#run de model again!
#popsize_r0_m0.optimize(method="L-BFGS-B")

#now do a few repeats
results_r0_m0 = []
n_runs = 25
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    popsize_r0_m0.set_params(randomize=True)
    results_r0_m0.append(popsize_r0_m0.optimize(method="L-BFGS-B", options={"maxiter":200}))
# sort results according to log likelihood, pick the best (largest) one
best_result_r0_m0 = sorted(results_r0_m0, key=lambda r: r.log_likelihood)[-1]
popsize_r0_m0.set_params(best_result_r0_m0.parameters)
best_result_r0_m0
#AIC
for model in [popsize_r0_m0]:
    lik = model.log_likelihood()
    nparams = len(model.get_params())
    aic = 2*nparams - 2*lik
    print("AIC {}".format(aic))

#ok let's try a population bottleneck model in peruvianus with variable pop sizes
popsize_r0_m1 = momi.DemographicModel(N_e=2.5e5)
popsize_r0_m1.set_data(sfs)
#pop size parameters
popsize_r0_m1.add_size_param("n_peruvianus")
popsize_r0_m1.add_size_param("n_sincipitalis")
popsize_r0_m1.add_size_param("n_rufifrons")
popsize_r0_m1.add_size_param("n_specularis")
#this is the previous peruvianus pop size-- if it is smaller than the one above then it is a bottleneck
#in this version of the model the "bottleneck" starts at the split, which seems justifiable
#but we can play around with that
popsize_r0_m1.add_size_param("n_peruvianus_bottleneck")
popsize_r0_m1.add_leaf("peruvianus", N="n_peruvianus")
#now add the bottleneck event
popsize_r0_m1.add_time_param("tb")
popsize_r0_m1.set_size("peruvianus", N="n_peruvianus_bottleneck", t="tb")
#and make the rest of the tree
popsize_r0_m1.add_leaf("sincipitalis", N="n_sincipitalis")
popsize_r0_m1.add_time_param("t1", lower_constraints=["tb"])
popsize_r0_m1.move_lineages("peruvianus", "sincipitalis", t="t1")
popsize_r0_m1.add_leaf("rufifrons", N= "n_rufifrons")
popsize_r0_m1.add_time_param("t2", lower_constraints=["t1"])
popsize_r0_m1.move_lineages("sincipitalis", "rufifrons", t="t2")
popsize_r0_m1.add_leaf("specularis", N="n_specularis")
popsize_r0_m1.add_time_param("t3", lower_constraints=["t2"])
popsize_r0_m1.move_lineages("rufifrons", "specularis", t="t3")
#run de model again!
#popsize_r0_m1.optimize(method="L-BFGS-B")

#now do a few repeats
results_r0_m1 = []
n_runs = 25
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    popsize_r0_m1.set_params(randomize=True)
    results_r0_m1.append(popsize_r0_m1.optimize(method="L-BFGS-B", options={"maxiter":200}))
# sort results according to log likelihood, pick the best (largest) one
best_result_r0_m1 = sorted(results_r0_m1, key=lambda r: r.log_likelihood)[-1]
popsize_r0_m1.set_params(best_result_r0_m1.parameters)
best_result_r0_m1
#AIC
for model in [popsize_r0_m1]:
    lik = model.log_likelihood()
    nparams = len(model.get_params())
    aic = 2*nparams - 2*lik
    print("AIC {}".format(aic))


#ok let's try a population bottleneck model in sincipitalis with variable pop sizes
popsize_r0_m2 = momi.DemographicModel(N_e=2.5e5)
popsize_r0_m2.set_data(sfs)
#pop size parameters
popsize_r0_m2.add_size_param("n_peruvianus")
popsize_r0_m2.add_size_param("n_sincipitalis")
popsize_r0_m2.add_size_param("n_rufifrons")
popsize_r0_m2.add_size_param("n_specularis")
#this is the previous sincipitalis pop size-- if it is smaller than the one above then it is a bottleneck
#in this version of the model the "bottleneck" starts at the split, which seems justifiable
#but we can play around with that
popsize_r0_m2.add_size_param("n_sincipitalis_bottleneck")
popsize_r0_m2.add_leaf("sincipitalis", N="n_sincipitalis")
#now add the bottleneck event
popsize_r0_m2.add_time_param("tb")
popsize_r0_m2.set_size("sincipitalis", N="n_sincipitalis_bottleneck", t="tb")
#and make the rest of the tree
popsize_r0_m2.add_leaf("peruvianus", N="n_peruvianus")
popsize_r0_m2.add_time_param("t1", lower_constraints=["tb"])
popsize_r0_m2.move_lineages("peruvianus", "sincipitalis", t="t1")
popsize_r0_m2.add_leaf("rufifrons", N= "n_rufifrons")
popsize_r0_m2.add_time_param("t2", lower_constraints=["t1"])
popsize_r0_m2.move_lineages("sincipitalis", "rufifrons", t="t2")
popsize_r0_m2.add_leaf("specularis", N="n_specularis")
popsize_r0_m2.add_time_param("t3", lower_constraints=["t2"])
popsize_r0_m2.move_lineages("rufifrons", "specularis", t="t3")
#run de model again!
#popsize_r0_m2.optimize(method="L-BFGS-B")

#now do a few repeats
results_r0_m2 = []
n_runs = 25
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    popsize_r0_m2.set_params(randomize=True)
    results_r0_m2.append(popsize_r0_m2.optimize(method="L-BFGS-B", options={"maxiter":200}))
# sort results according to log likelihood, pick the best (largest) one
best_result_r0_m2 = sorted(results_r0_m2, key=lambda r: r.log_likelihood)[-1]
popsize_r0_m2.set_params(best_result_r0_m2.parameters)
best_result_r0_m2
#AIC
for model in [popsize_r0_m2]:
    lik = model.log_likelihood()
    nparams = len(model.get_params())
    aic = 2*nparams - 2*lik
    print("AIC {}".format(aic))


#ok let's try a population bottleneck model in rufifrons with variable pop sizes
popsize_r0_m3 = momi.DemographicModel(N_e=2.5e5)
popsize_r0_m3.set_data(sfs)
#pop size parameters
popsize_r0_m3.add_size_param("n_peruvianus")
popsize_r0_m3.add_size_param("n_sincipitalis")
popsize_r0_m3.add_size_param("n_rufifrons")
popsize_r0_m3.add_size_param("n_specularis")
#this is the previous rufifrons pop size-- if it is smaller than the one above then it is a bottleneck
#in this version of the model the "bottleneck" starts at the split, which seems justifiable
#but we can play around with that
popsize_r0_m3.add_size_param("n_rufifrons_bottleneck")
#add all leaves
popsize_r0_m3.add_leaf("sincipitalis", N="n_sincipitalis")
popsize_r0_m3.add_leaf("peruvianus", N="n_peruvianus")
popsize_r0_m3.add_leaf("rufifrons", N= "n_rufifrons")
popsize_r0_m3.add_leaf("specularis", N="n_specularis")
#add bottleneck
popsize_r0_m3.add_time_param("tb")
popsize_r0_m3.set_size("rufifrons", N="n_rufifrons_bottleneck", t="tb")
#and make the rest of the tree
popsize_r0_m3.add_time_param("t1")
popsize_r0_m3.move_lineages("peruvianus", "sincipitalis", t="t1")
popsize_r0_m3.add_time_param("t2", lower_constraints=["t1", "tb"])
popsize_r0_m3.move_lineages("sincipitalis", "rufifrons", t="t2")
popsize_r0_m3.add_time_param("t3", lower_constraints=["t2"])
popsize_r0_m3.move_lineages("rufifrons", "specularis", t="t3")
#run de model again!
#popsize_r0_m3.optimize(method="L-BFGS-B")

#now do a few repeats
results_r0_m3 = []
n_runs = 25
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    popsize_r0_m3.set_params(randomize=True)
    results_r0_m3.append(popsize_r0_m3.optimize(method="L-BFGS-B", options={"maxiter":200}))
# sort results according to log likelihood, pick the best (largest) one
best_result_r0_m3 = sorted(results_r0_m3, key=lambda r: r.log_likelihood)[-1]
popsize_r0_m3.set_params(best_result_r0_m3.parameters)
best_result_r0_m3
#AIC
for model in [popsize_r0_m3]:
    lik = model.log_likelihood()
    nparams = len(model.get_params())
    aic = 2*nparams - 2*lik
    print("AIC {}".format(aic))


#and finally we have the population size change in specularis
popsize_r0_m4 = momi.DemographicModel(N_e=2.5e5)
popsize_r0_m4.set_data(sfs)
#pop size parameters
popsize_r0_m4.add_size_param("n_peruvianus")
popsize_r0_m4.add_size_param("n_sincipitalis")
popsize_r0_m4.add_size_param("n_rufifrons")
popsize_r0_m4.add_size_param("n_specularis")
#this is the previous specularis pop size-- if it is smaller than the one above then it is a bottleneck
#in this version of the model the "bottleneck" starts at the split, which seems justifiable
#but we can play around with that
popsize_r0_m4.add_size_param("n_specularis_bottleneck")
#add all leaves
popsize_r0_m4.add_leaf("sincipitalis", N="n_sincipitalis")
popsize_r0_m4.add_leaf("peruvianus", N="n_peruvianus")
popsize_r0_m4.add_leaf("rufifrons", N= "n_rufifrons")
popsize_r0_m4.add_leaf("specularis", N="n_specularis")
#add bottleneck
popsize_r0_m4.add_time_param("tb")
popsize_r0_m4.set_size("specularis", N="n_specularis_bottleneck", t="tb")
#and make the rest of the tree
popsize_r0_m4.add_time_param("t1")
popsize_r0_m4.move_lineages("peruvianus", "sincipitalis", t="t1")
popsize_r0_m4.add_time_param("t2", lower_constraints=["t1"])
popsize_r0_m4.move_lineages("sincipitalis", "rufifrons", t="t2")
popsize_r0_m4.add_time_param("t3", lower_constraints=["t2", "tb"])
popsize_r0_m4.move_lineages("rufifrons", "specularis", t="t3")
#run de model again!
#popsize_r0_m4.optimize(method="L-BFGS-B")

#now do a few repeats
results_r0_m4 = []
n_runs = 25
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    popsize_r0_m4.set_params(randomize=True)
    results_r0_m4.append(popsize_r0_m4.optimize(method="L-BFGS-B", options={"maxiter":200}))
# sort results according to log likelihood, pick the best (largest) one
best_result_r0_m4 = sorted(results_r0_m4, key=lambda r: r.log_likelihood)[-1]
popsize_r0_m4.set_params(best_result_r0_m4.parameters)
best_result_r0_m4
#AIC
for model in [popsize_r0_m4]:
    lik = model.log_likelihood()
    nparams = len(model.get_params())
    aic = 2*nparams - 2*lik
    print("AIC {}".format(aic))

#this is the combination of migration models 5 and 6
combo_r2_m1= momi.DemographicModel(N_e=2.5e5)
combo_r2_m1.set_data(sfs)
#pop size parameters
combo_r2_m1.add_size_param("n_peruvianus")
combo_r2_m1.add_size_param("n_sincipitalis")
combo_r2_m1.add_size_param("n_rufifrons")
combo_r2_m1.add_size_param("n_specularis")
#migration time parameters
combo_r2_m1.add_time_param("tm1")
combo_r2_m1.add_time_param("tm2")
#make the tree, with pop size parameters when we add leaves
combo_r2_m1.add_leaf("peruvianus", N="n_peruvianus")
combo_r2_m1.add_leaf("sincipitalis", N="n_sincipitalis")
combo_r2_m1.add_leaf("rufifrons", N= "n_rufifrons")
combo_r2_m1.add_leaf("specularis", N="n_specularis")
#split time parameters. tm1 and tm2 have to happen before t2 but not necessarily before t1
combo_r2_m1.add_time_param("t1")
combo_r2_m1.add_time_param("t2", lower_constraints=["t1", "tm1", "tm2"])
combo_r2_m1.add_time_param("t3", lower_constraints=["t2"])
#the actual splitting events
combo_r2_m1.move_lineages("peruvianus", "sincipitalis", t="t1")
combo_r2_m1.move_lineages("sincipitalis", "rufifrons", t="t2")
combo_r2_m1.move_lineages("rufifrons", "specularis", t="t3")
#the two migration events
combo_r2_m1.move_lineages("rufifrons", "specularis", t="tm1", p=0.1)
combo_r2_m1.move_lineages("specularis", "rufifrons", t="tm2", p=0.1)
#not doing the one test run because that adds time
#combo_r2_m1.optimize(method="L-BFGS-B")
#set up for 25 runs
results_r2_m1 = []
n_runs = 25
#do the 25 runs
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    combo_r2_m1.set_params(randomize=True)
    results_r2_m1.append(combo_r2_m1.optimize(method="L-BFGS-B", options={"maxiter":200}))
# sort results according to log likelihood, pick the best (largest) one
best_result_r2_m1 = sorted(results_r2_m1, key=lambda r: r.log_likelihood)[-1]
combo_r2_m1.set_params(best_result_r2_m1.parameters)
best_result_r2_m1
#calculate the AIC
import numpy as np

lik = combo_r2_m1.log_likelihood()
nparams = len(combo_r2_m1.get_params())
aic = 2*nparams - 2*lik
print("AIC {}".format(aic))


#this is the combination of migration models 5 and 6 and combo model 2
combo_r2_m2= momi.DemographicModel(N_e=2.5e5)
combo_r2_m2.set_data(sfs)
#pop size parameters
combo_r2_m2.add_size_param("n_peruvianus")
combo_r2_m2.add_size_param("n_sincipitalis")
combo_r2_m2.add_size_param("n_rufifrons")
combo_r2_m2.add_size_param("n_specularis")
#migration time parameters
combo_r2_m2.add_time_param("tm1")
combo_r2_m2.add_time_param("tm2")
#different pop size and time parameters
combo_r2_m2.add_size_param("n_sincipitalis_bottleneck")
combo_r2_m2.add_time_param("tb")
#make the tree, with pop size parameters when we add leaves
combo_r2_m2.add_leaf("peruvianus", N="n_peruvianus")
combo_r2_m2.add_leaf("sincipitalis", N="n_sincipitalis")
combo_r2_m2.add_leaf("rufifrons", N= "n_rufifrons")
combo_r2_m2.add_leaf("specularis", N="n_specularis")
#population size change
combo_r2_m2.set_size("sincipitalis", N="n_sincipitalis_bottleneck", t="tb")
#split time parameters. tm1 and tm2 have to happen before t2 but not necessarily before t1
#tb happens before t1
combo_r2_m2.add_time_param("t1", lower_constraints=["tb"])
combo_r2_m2.add_time_param("t2", lower_constraints=["t1", "tm1", "tm2"])
combo_r2_m2.add_time_param("t3", lower_constraints=["t2"])
#the actual splitting events
combo_r2_m2.move_lineages("peruvianus", "sincipitalis", t="t1")
combo_r2_m2.move_lineages("sincipitalis", "rufifrons", t="t2")
combo_r2_m2.move_lineages("rufifrons", "specularis", t="t3")
#the two migration events
combo_r2_m2.move_lineages("rufifrons", "specularis", t="tm1", p=0.1)
combo_r2_m2.move_lineages("specularis", "rufifrons", t="tm2", p=0.1)
#not doing the one test run because that adds time
#combo_r2_m2.optimize(method="L-BFGS-B")
#set up for 25 runs
results_r2_m2 = []
n_runs = 25
#do the 25 runs
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    combo_r2_m2.set_params(randomize=True)
    results_r2_m2.append(combo_r2_m2.optimize(method="L-BFGS-B", options={"maxiter":200}))
# sort results according to log likelihood, pick the best (largest) one
best_result_r2_m2 = sorted(results_r2_m2, key=lambda r: r.log_likelihood)[-1]
combo_r2_m2.set_params(best_result_r2_m2.parameters)
best_result_r2_m2

lik = combo_r2_m2.log_likelihood()
nparams = len(combo_r2_m2.get_params())
aic = 2*nparams - 2*lik
print("AIC {}".format(aic))
