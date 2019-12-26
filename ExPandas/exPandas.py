import pandas

df1 = pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Value"],index=["First","Second"])
df2 = pandas.DataFrame([{"Name":"Jhon","Surname":"Johns"},{"Name":"Jack","Surname":"Bonb"}])
df1.mean()
df1.mean().mean()
df1.Price.mean()
print (df1)