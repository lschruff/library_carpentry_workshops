# install missing modules directly inside jupyter notebook
# only needs to be executed once, is then available until it is uninstalled
# !pip install matplotlib

# import matplotlib might be necessary
# import matplotlib


# this command displays histograms directly in the notebook
# %matplotlib inline

# plot histogram for column "hasData_size"

# Option 1:
# df_frl_file_data["hasData_size"].hist()

# Option 2: adding "matplotlib.pyplot.show()" might be needed
# matplotlib.pyplot.show(df_frl_file_data["hasData_size"].hist())
