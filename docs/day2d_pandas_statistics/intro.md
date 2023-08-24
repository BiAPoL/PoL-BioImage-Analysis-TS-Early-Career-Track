# Working with tabular data and Statistics

In this chapter we will explore working with tabular data using the [pandas library](https://pandas.pydata.org/). We will explore tabular datasets, extract rows and columns from tables, eliminate NaNs and do basic descriptive statistics on measurements. We will also combine tables and manipulate them to make them easy to be grouped and have functions applied.

Following tables, we will teach you how to apply statistical methods for hypothesis testing to your data, like normality tests, t-tests, analysis of variance, etc.

To get the most of this and the follwoing chapters' content running in your computer, we ask you to install some additional packages to the course environment.

 * seaborn (load dataset titanic from seaborn package)
 * pivottablejs (for more easy pivot tables and fast simple visualization)
 * watermark (documenting version of packages)
 * statannotations (for adding statistical test results to plots)
 * scikit_posthocs (for post-tests)

Open a terminal, activate the environment and install the necessary additional packages by running the commands below:

```
mamba activate devbio-napari-env

pip install scikit_posthocs statannotations watermark pivottablejs seaborn==0.12.2
```
