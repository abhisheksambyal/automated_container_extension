# automated_container_extension
Fills out the container extension form automatically. (Specific to IIT Ropar)

## Download the chrome driver from the website below (make sure your google chrome browser and chrome driver version is same)
Link: https://chromedriver.chromium.org/

## Steps:
Extract the zip file.  
Store the extracted directory and main.py file at same level (depth).  
<pre>
Eg. - dir1  
       |-> chromedriver.zip  
       |-> chromedriver (zip extracted directory)  
       |-> main.py  
</pre>

## Step for setting up the conda environment:
1. conda create --name container python=3.6
2. conda activate container
3. pip install selenium
4. conda install pandas

## Steps to update user_data.csv file. It contains your requirement details.  
1. Change the values in **user_data.csv** as per your need. Please look at the *container google form* for valid values/entries.
2. Text box entries could be anything. Refrain yourself from using ";" (semicolon). It is used as a delimiter for extracting data.
3. Adding the value of *dropdown entries* in the csv file has to be the same as the *container google form* mentioned. Make sure you write the text(string) as it is, including spaces, commas, quotes, etc.  

*Note: When you open user_data.csv in any word processor, make sure to select **;** (semicolon) as a separator. Otherwise, you will see multiple entries merging into one column.*


If you are still facing an issue, reach out to me here *abhishek [dot] 19csz0001 [at] iitrpr[dot]ac[dot]in*
