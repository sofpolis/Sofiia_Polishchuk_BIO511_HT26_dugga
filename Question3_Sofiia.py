import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#a) and b)
#reading in the .csv file
cnv = pd.read_csv("cnv_data.csv")

#making a scatterplot with sns
fig1 = sns.scatterplot(cnv, x="position_mb", y="log2_ratio")
plt.tight_layout()
plt.savefig("fig1.png")

#c)

input_file = sys.argv[1] #the input file should be stated by the user as first argument when running the script
output_file = sys.argv[2] #the output file should be stated by the user as second argument when running the script

cnv = pd.read_csv(input_file)
fig2 = sns.scatterplot(cnv, x="position_mb", y="log2_ratio")
plt.tight_layout()
plt.savefig(output_file)
