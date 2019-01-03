import pandas as pd
from . models import *

excel_file = 'documentations/Model_mstr.xls'
movies = pd.read_excel(excel_file)
movies_sheet1 = pd.read_excel(excel_file, sheet_name=0)

"""i=0;

for rwo in movies_sheet1.axes[0]:
	j=0
	k=0
	for clo in movies_sheet1.columns.values:
		jbh = movies_sheet1.iat[i,k]
		jbh = str(jbh)
		if jbh != "nan":
				if j == 0:
					pass
				if clo == "EXSHOWROOMSLAB":
					m = k
				if jbh == "STAR (ELECTRIC-START )X PRESS":
					n = i
					break
				j=j+1
		k=k+1
	i=i+1
print(i, j)
"""

a=[]
for t in range(0,2764):
		keyword = ""
		keyword = keyword.strip().upper()
		name = movies_sheet1.iat[t,1]
		name = str(name).strip().upper()
		jbh = name
		'''["name",
								"exprice",
								"make code",
								"model code",
								"Cubic Capacity"
								]'''
		if jbh != "nan":
				model = jbh1 = movies_sheet1.iat[t,3].strip().upper()
				if jbh1.strip().upper().find(keyword) != -1 or jbh.strip().upper().find(keyword) != -1:
					cc = str(movies_sheet1.iat[t,5]).strip().upper()
					exprice = str(movies_sheet1.iat[t,24]).strip().upper()

					name1 = str(str(name).strip().upper()+" - "+ str(model).strip().upper()+ " ("+ str(cc).strip().upper()+ "CC)").strip().upper()
					makes = Make.objects.filter(name=name, name1=name1, model = model, cc = cc)
					if makes.count() == 0:
						make = Make.objects.create(name1=name1, name=name, model = model, cc = cc,
							namec = movies_sheet1.iat[t,2], exprice = float(exprice))
						if str(make.exprice) == "nan":
								make.exprice = 0
						make.save()
						print()
					else:
						make = Make.objects.get(name1=name1, name=name, model = model, cc = cc)
						make.modelc = 31

						#namec = makec
						make.namec = movies_sheet1.iat[t,2]
						make.save()
						print()
						print("Already", movies_sheet1.iat[t,2])
						#print(make.name)
						#print(make.name1)
						try:
							make.exprice = float(exprice)
							if str(make.exprice) == "nan":
								make.exprice = 0
							make.save()
							print("floated",make.exprice)
						except:
							print()
							print(make.exprice)
							pass
						#print(make.model)
						#print(make.cc)
						#print()
						#print()
