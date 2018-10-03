#python
import lx
import copy

itemNum = lx.eval("query sceneservice item.N ? ");
itemNumList = range(0, itemNum);

itemList = {};

for item in itemNumList:
	itemID = lx.eval("query sceneservice item.id ? %s" %item);
	itemName = lx.eval("query sceneservice item.name ? %s" %item);
	itemList[item] = itemID + ' ' + itemName;
#itemList.append(itemID);
lx.out(itemList);


selItems = lx.evalN("query sceneservice selection ? all")


lis = list(selItems) #tuple to list conversion
lx.out(selItems) #tuple
lx.out(lis) #list

cha = []

for item in lis:
	lx.eval("select.subitem %s add mesh 1 1" %item)
	newSel =lx.eval("query sceneservice selection ? all")
	for element in newSel:
		if element not in cha:
			cha.append(element)
	
chaName =[]	
lx.out(cha)
for item in cha:
	itemName = lx.eval("query sceneservice item.name ? %s" %item)
	lx.out(itemName)
	chaName.append(itemName)
lx.out(chaName)	
for item in cha:
	lx.eval("select.subitem %s remove mesh 1 1" %item)
lx.out(cha)
chm = copy.copy(cha)
vcha = copy.copy(cha)
lx.out(chm)
for a in cha:
	aName = lx.eval("query sceneservice item.name ? %s" %a)
	chm.remove(a)
	#lx.out(chm)
	lx.out(aName)
	for b in chm:
		bName = lx.eval("query sceneservice item.name ? %s" %b)
		if str(bName) + '_2' == str(aName): 
			
			lx.eval("select.subitem %s set mesh " %a)
			lx.eval("select.subitem %s add mesh " %b)
			lx.eval("constraintTransform add pos false")
			lx.eval("select.subitem %s set mesh " %a)
			lx.eval("select.subitem %s add mesh " %b)
			lx.eval("constraintTransform add rot false")


for item in vcha:
	lx.eval("layer.setVisibility %s true" %item)
lx.out(vcha)




    





	 
  #lx.out(chName)	#aha.append(ha);
	#lx.out(ha);
#lx.out(aha)

