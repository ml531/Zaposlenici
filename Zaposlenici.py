import streamlit as st
from deta import Deta
def login():
	firstName = st.text_input("Enter first name", autocomplete="Matko")
	lastName = st.text_input("Enter last name", autocomplete="Matković")
	password = st.text_input("Enter password", type="password", autocomplete=None)
	role = st.radio('Pick your role:', ['Director', 'Manager', "Worker"])
	col1, col2, col3 = st.columns([1,1,1])
	with col1:
		st.write("")
	with col2:
		btn1 = st.button('Login')
	with col3:
		st.write("")
	if btn1:
		id = 0
		for x in db1_content:
			if(firstName == x.get("firstName") and lastName == x.get("lastName") and password == x.get("password") and role == x.get("role")):
				id = x.get("id")
				for y in db2_content:
					if(id == y.get("id")):
						db2.update({"log": True}, y.get("key"))
						st.rerun()
		if(id == 0):
			st.error("Wrong input!")


def Director():
	pom = 0
	colu1, colu2, colu3, colu4, colu5 = st.columns([1,1,1,1,1])
	with colu1:
		st.write("**First name**")
	with colu2:
		st.write("**Last name**")
	with colu3:
		st.write("**Hours**")
	with colu4:
		st.write("**Paycheck**")
	with colu5:
		st.write("**Role**")
	st.write("")
	for l in db1_content:
		col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
		with col1:
			st.write(l.get("firstName"))
		with col2:
			st.write(l.get("lastName"))
		with col3:
			st.write(l.get("hours"))
		with col4:
			st.write(l.get("paycheck"))
		with col5:
			st.write(l.get("role"))
	st.header("Add or Delete user")
	co1, co2 = st.columns([1,1])
	with co1:
		fN = st.text_input("First name", autocomplete = "M")
	with co2:
		lN = st.text_input("Last name", autocomplete = "M")
	c1, c2, c3, c4 = st.columns([1,1,1,1])
	with c1:
		st.write("")
	with c2:
		btn3 = st.button("Add")
	with c3:
		btn4 = st.button("Delete")
	with c4:
		st.write("")
	id = 0
	if btn3:
		if(fN == "" or lN == ""):
			st.error("User must have first and last name!")
			pom = 1
		for j in db1_content:
			if(j.get("firstName") == fN and j.get("lastName") == lN):
				st.error("User alredy exist!")
				pom = 1
			if(j.get("id") > id):
				id = j.get("id")
		if(pom == 0):
			id = id + 1
			db1.put({"firstName": fN, "lastName": lN, "id" : id})
			db2.put({"id": id, "log" : False})
			st.rerun()
		pom = 0
	if btn4:
		if(fN == "" or lN == ""):
			st.error("User must have first and last name!")
			pom = 1
		else:
			for j in db1_content:
				if(j.get("firstName") == fN and j.get("lastName") == lN):
					for k in db2_content:
						if(k.get("id") == j.get("id")):
							db2.delete(k.get("key"))
					db1.delete(j.get("key"))
					st.rerun()
		pom = 0
	st.header("Update user")
	st.write("Enter first and last name of user you want to update: ")
	co1, co2 = st.columns([1,1])
	with co1:
		f1 = st.text_input("First name", autocomplete = "Ma")
	with co2:
		l1 = st.text_input("Last name", autocomplete = "Ma")
	st.write("Enter attributes you want to update: ")
	f = st.text_input("First name", autocomplete="O")
	l = st.text_input("Last name", autocomplete="O")
	p = st.text_input("Password", type="password", autocomplete=None)
	y = st.number_input("Paycheck", step = 1, min_value = 0, max_value = 100000)
	h = st.number_input("Worked hours", step = 1, min_value = 0, max_value = 200)
	r = st.radio('Role:', ['Director', 'Manager', "Worker"])
	a1, a2, a3 = st.columns([1,1,1])
	with a1:
		st.write("")
	with a2:
		btn5 = st.button("Update")
	with a3:
		st.write("")
	if btn5:
		if(f1 == "" or l1 == ""):
			st.error("User must have first and last name!")
			pom = 1
		if(pom == 0):
			for z in db1_content:
				if(z.get("firstName") == f1 and z.get("lastName") == l1):
					if(f != "" and l != ""):
						db1.update({"firstName": f, "lastName" : l}, z.get("key"))
					db1.update({"password": p, "paycheck" : y, "hours" : h, "role" : r}, z.get("key"))
						
				if(z.get("firstName") == f1 and z.get("lastName") == l1):		
					for o in db2_content:
						if(o.get("id") == z.get("id")):
							db2.update({"role": r}, o.get("key"))
			st.rerun()
		pom = 0
	d1, d2, d3 = st.columns([1,1,1])
	with d1:
		st.write("")
	with d2:
		btn7 = st.button('Logout')
	with d3:
		st.write("")
	if btn7:
		for r in db2_content:
			if(r.get("log") == True):
				db2.update({"log" : False}, r.get("key"))
				st.rerun()
def Manager():
	pom = 0
	colu1, colu2, colu3, colu4, colu5 = st.columns([1,1,1,1,1])
	with colu1:
		st.write("**First name**")
	with colu2:
		st.write("**Last name**")
	with colu3:
		st.write("**Hours**")
	with colu4:
		st.write("**Paycheck**")
	with colu5:
		st.write("**Role**")
	st.write("")
	for l in db1_content:
		if(l.get("role") != "Director"):
			col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
			with col1:
				st.write(l.get("firstName"))
			with col2:
				st.write(l.get("lastName"))
			with col3:
				st.write(l.get("hours"))
			with col4:
				st.write(l.get("paycheck"))
			with col5:
				st.write(l.get("role"))
	st.header("Add or Delete user")
	co1, co2 = st.columns([1,1])
	with co1:
		fN = st.text_input("First name", autocomplete = "M")
	with co2:
		lN = st.text_input("Last name", autocomplete = "M")
	c1, c2, c3, c4 = st.columns([1,1,1,1])
	with c1:
		st.write("")
	with c2:
		btn3 = st.button("Add")
	with c3:
		btn4 = st.button("Delete")
	with c4:
		st.write("")
	id = 0
	if btn3:
		if(fN == "" or lN == ""):
			st.error("User must have first and last name!")
			pom = 1
		for j in db1_content:
			if(j.get("firstName") == fN and j.get("lastName") == lN):
				st.error("User alredy exist!")
				pom = 1
			if(j.get("id") > id):
				id = j.get("id")
		if(pom == 0):
			id = id + 1
			db1.put({"firstName": fN, "lastName": lN, "id" : id})
			db2.put({"id": id, "log" : False})
			st.rerun()
		pom = 0
	if btn4:
		if(fN == "" or lN == ""):
			st.error("User must have first and last name!")
			pom = 1
		else:
			for j in db1_content:
				if(j.get("firstName") == fN and j.get("lastName") == lN):
					if(j.get("role") == "Director"):
						st.error("Not authorized")
					else:
						for k in db2_content:
							if(k.get("id") == j.get("id")):
								db2.delete(k.get("key"))
						db1.delete(j.get("key"))
						st.rerun()
		pom = 0
	st.header("Update user")
	st.write("Enter first and last name of user you want to update: ")
	co1, co2 = st.columns([1,1])
	with co1:
		f1 = st.text_input("First name", autocomplete = "Ma")
	with co2:
		l1 = st.text_input("Last name", autocomplete = "Ma")
	st.write("Enter attributes you want to update: ")
	f = st.text_input("First name", autocomplete="O")
	l = st.text_input("Last name", autocomplete="O")
	p = st.text_input("Password", type="password", autocomplete=None)
	y = st.number_input("Paycheck", step = 1, min_value = 0, max_value = 100000)
	h = st.number_input("Worked hours", step = 1, min_value = 0, max_value = 200)
	r = st.radio('Role:', ['Manager', "Worker"])
	a1, a2, a3 = st.columns([1,1,1])
	with a1:
		st.write("")
	with a2:
		btn5 = st.button("Update")
	with a3:
		st.write("")
	if btn5:
		if(f1 == "" or l1 == ""):
			st.error("User must have first and last name!")
			pom = 1
		if(pom == 0):
			for z in db1_content:
				if(z.get("firstName") == f1 and z.get("lastName") == l1):
					if(f != "" and l != ""):
						db1.update({"firstName": f, "lastName" : l}, z.get("key"))
					db1.update({"password": p, "paycheck" : y, "hours" : h, "role" : r}, z.get("key"))
				if(z.get("firstName") == f1 and z.get("lastName") == l1):		
					for o in db2_content:
						if(o.get("id") == z.get("id")):
							db2.update({"role": r}, o.get("key"))
			st.rerun()
		pom = 0
	d1, d2, d3 = st.columns([1,1,1])
	with d1:
		st.write("")
	with d2:
		btn7 = st.button('Logout')
	with d3:
		st.write("")
	if btn7:
		for r in db2_content:
			if(r.get("log") == True):
				db2.update({"log" : False}, r.get("key"))
				st.rerun()

def Worker():
	st.header("Your data ")
	for m in db2_content:
		if(m.get("log") == True):
			for n in db1_content:
				if(m.get("id") == n.get("id")):
					colu1, colu2, colu3, colu4, colu5 = st.columns([1,1,1,1,1])
					with colu1:
						st.write("**First name**")
					with colu2:
						st.write("**Last name**")
					with colu3:
						st.write("**Hours**")
					with colu4:
						st.write("**Paycheck**")
					with colu5:
						st.write("**Role**")
					st.write("")
					col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
					with col1:
						st.write(n.get("firstName"))
					with col2:
						st.write(n.get("lastName"))
					with col3:
						st.write(n.get("hours"))
					with col4:
						st.write(n.get("paycheck"))
					with col5:
						st.write(n.get("role"))
	d1, d2, d3 = st.columns([1,1,1])
	with d1:
		st.write("")
	with d2:
		btn7 = st.button('Logout')
	with d3:
		st.write("")
	if btn7:
		for r in db2_content:
			if(r.get("log") == True):
				db2.update({"log" : False}, r.get("key"))
				st.rerun()

chk = 0
deta = Deta("a0kzff1mwsv_XyUaewTdfsbv2DizbbcD2LsDTAwBypfs")
db1 = deta.Base("user")
db2 = deta.Base("logged")
db1_content = db1.fetch().items
db2_content = db2.fetch().items
chk = 0
for q in db2_content:
	if(q.get("log")):
		if(q.get("role") == "Director"):
			Director()
		elif(q.get("role") == "Manager"):
			Manager()
		elif(q.get("role") == "Worker"):
			Worker()
		else:
			st.error("Wrong role")
		chk = 1
if(chk == 0):
	login()

