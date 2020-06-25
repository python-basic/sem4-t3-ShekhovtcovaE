
class NewRegistration():
    def __init__(self, fname="", sname="", email="", password="", address = "", sorceinfo = "",  postalcode = "", city = "", country = "", regtype = "", affiliation = ""):
        self.__fname, self.__email, self.__sname, self.__password, self.__sorceinfo, self.__address, self.__city, self.__country, self.__regtype, self.__affiliation, self.__postalcode = fname, email, sname, password, sorceinfo, address, city, country, regtype, affiliation, postalcode
 
    @property
    def fname(self):
        return self.__fname
    @fname.setter
    def fname(self, new_fname):
        if (new_fname != ""):
            self.__fname = new_fname
        else:
            raise ValueError("Имя не может быть пустым")
    @property
    def sname(self):
        return self.__sname

    @sname.setter
    def sname(self, new_sname):
        if (new_sname != ""):
            self.__sname = new_sname
        else:
            raise ValueError("Фамилия не может быть пустой")
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if len(new_password) < 8:
            raise ValueError("Произошла ошибка, пароль введен некорректно")
        else:
            self.__password = new_password
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        if not isinstance(new_email, str):
            raise ValueError("Произошла ошибка, e-mail введен некорректно")
        else:
            self.__email = new_email

    @property
    def sorceinfo(self):
        return self.__sorceinfo

    @sorceinfo.setter
    def sorceinfo(self, new_sorceinfo):
        if (isinstance(new_sorceinfo, str)) and (len(new_sorceinfo) > 100):
            self.__sorceinfo = new_sorceinfo
        else:
            raise ValueError("Информация введена некорректно")

    @property
    def postalcode(self):
        return self.__postalcode

    @postalcode.setter
    def postalcode(self, new_postalcode):
        if not isinstance(new_postalcode, str):
            raise ValueError("Индекс введен некорректно")
        else:
            self.__postalcode = new_postalcode
    
    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, new_city):
        if not isinstance(new_city, str):
            raise ValueError("Город введен некорректно")
        else:
            self.__city = new_city
    
    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, new_country):
        if not isinstance(new_country, str):
            raise ValueError("Государство введено некорректно")
        else:
            self.__country = new_country
   
    @property
    def affiliation(self):
        return self.__affiliation

    @affiliation.setter
    def affiliation(self, new_affiliation):
        if (isinstance(new_affiliation, str)) and (len(new_affiliation) > 150):
            self.__affiliation = new_affiliation
        else:
            raise ValueError("Аффиляция введена некорректно")
    
    @property
    def address(self):
        return self.__address
        
    @address.setter
    def adress(self, new_address):
        if (isinstance(new_address, str)) or (len(new_address) > 10):
            self.__address = new_address
        else:
            raise ValueError("Адрес должен быть длиннее 10 символов")
    
    @property
    def regtype(self):
        return self.__regtype
        
    @regtype.setter
    def regtype(self, new_regtype):
        if not (isinstance(new_regtype, str)) or (new_regtype != "IEEE members") or (new_regtype != "full registration"):
            raise ValueError("Информация введена некорректно")
        else:
            self.__regtype = new_regtype
    def __repr__(self):
        str1 = 'Имя: {0}\nФамилия: {1}\nE-mail: {2}\nПароль: {3}\nАдрес: {4}\nИндекс: {5}\n'
        str2 = 'Откуда узнали о нас: {6}\nГород: {7}\nСтрана: {8}\nТип регистрации: {9}\nАффилиация автора: {10}'
        return (str1 + str2).format(self.fname, self.sname, self.email, self.password, self.address, self.postalcode, self.sorceinfo, self.city,self.country, self.regtype, self.affiliation)
        
u1 = NewRegistration()
u1 = NewRegistration('Цинциннат','Ц.','chemodan@google.com','V5Y3I1OOO7','ул. Морг, 3','Рассказали друзья','0856547','Нижневартовск','Россия','IEEE members','Нет')
print(u1)
