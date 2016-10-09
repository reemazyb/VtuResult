class vtu_cbsc:
	def __init__(usn, sem):
		reg_url = "http://result.vtu.ac.in/cbcs_results2016.aspx?usn=" 
		result = {}

		reg_result = self.get_vtu_results(usn,sem,reg_url)

		if reg_result:
			"""
			Omkar to process this result(october 2016)
			"""



	def get_vtu_results(self, usn, sem, url):
		site=url+usn+"&sem="+sem
		req=requests.post(site)
		soup=BeautifulSoup(req.text,'lxml')
		try:
			marks_list=[]
			name=soup.findAll(attrs={"name":"txtName"})[0]['value']
			
			for i in range(1,9):
				#pdb.set_trace()
				num=str(i)
				try:
					subject=soup.findAll(attrs={"name":"txtSub"+num})[0]['value'].upper().strip().replace(',','')
					code= soup.findAll(attrs={"name":"txtCode"+num})[0]['value'].upper().strip()
					credits=soup.findAll(attrs={"name":"txtCredits"+num})[0]['value'].upper().strip()
					credits_earned=soup.findAll(attrs={"name":"txtCreditEarned"+num})[0]['value'].upper().strip()
					grade_letter=soup.findAll(attrs={"name":"txtGardeLetter"+num})[0]['value'].upper().strip()
					grade_points=soup.findAll(attrs={"name":"txtGP"+num})[0]['value'].upper().strip()
					credits_points=soup.findAll(attrs={"name":"txtCP"+num})[0]['value'].upper().strip()
					remarks=soup.findAll(attrs={"name":"txtRemarks"+num})[0]['value'].upper().strip()

					marks=[subject,code,credits,credits_earned,grade_letter,grade_points,credits_points,remarks]
					if marks:
						marks_list.append(marks)
					threshold=0
				except KeyError:
					break
			#pdb.set_trace()
			if marks_list:
				
		except KeyError:
			retun None