import re,os
def replaceText(filePath,oldContent,newContent):
	file = open(filePath,'r',encoding='utf-8')
	allLines = file.readlines()
	file.close()
	file = open(filePath,'w+',encoding='utf-8')
	for eachLine in allLines:
		content = re.sub(oldContent,newContent,eachLine)
		file.writelines(content)
	file.close()

fileList = os.listdir('_posts')

for file in fileList :
	if file.endswith('.md'):
		replaceText('_posts/'+file,'https://raw.githubusercontent.com/','https://cdn.staticaly.com/gh/')
		print(file)
