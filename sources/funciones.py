#FUNCIONES


#FUNCION PARA DEVOLVER CONTINENTES CUANDO LE DAMOS PAISES EN UN DF

def continente(pais):
    asia=['Kazakhstan', 'Kyrgyzstan', 'Tajikistan', 'Turkmenistan', 'Uzbekistan', 'China', 'Korea', 'Japan', 'Mongolia', 'Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Iran', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka','Brunei', 'Darussalam', 'Cambodia', 'Indonesia', 'Lao', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Timor-Leste', 'Viet Nam', 'Armenia', 'Azerbaijan', 'Bahrain', 'Cyprus', 'Georgia', 'Iraq', 'Israel', 'Jordan', 'Kuwait', 'Lebanon', 'Oman', 'Qatar', 'Saudi Arabia', 'Palestine', 'Syria', 'Turkey', 'United Arab Emirates', 'Yemen']
    europe= ['Albania' ,'Andorra' ,'Austria' ,'Belarus' ,'Belgium' ,'Bosnia Herzegovina' ,'Bulgaria' ,'Croatia' ,'Cyprus' ,'Czech' ,'Denmark' ,'Estonia' ,'Finland' ,'France' ,'Germany' ,'Greece' ,'Hungary' ,'Iceland' ,'Ireland' ,'Italy' ,'Latvia' ,'Liechtenstein' ,'Lithuania' ,'Luxembourg' ,'Malta' ,'Moldova' ,'Monaco' ,'Montenegro' ,'Netherlands' ,'North' ,'Macedonia' ,'Norway' ,'Poland' ,'Portugal' ,'Romania' ,'Russia' ,'San Marino' ,'Serbia' ,'Slovakia' ,'Slovenia' ,'Spain' ,'Sweden' ,'Switzerland' ,'Ukraine' ,'United Kingdom']
    africa=['Lesotho', 'Swaziland', 'Botswana', 'Namibia', 'South Africa', 'Angola', 'Cameroon', 'Equatorial Guinea', 'Gabon', 'Congo', 'Chad', 'Central African Republic', 'Congo', 'Sao Tome and Principe', 'Burundi', 'Eritrea', 'Madagascar', 'Reunion', 'Somalia', 'Comoros', 'Ethiopia', 'Rwanda', 'Djibouti', 'Kenya', 'Mayotte', 'Seychelles', 'Uganda', 'Mozambique', 'Zambia', 'Malawi', 'Tanzania', 'Zimbabwe', 'Benin', 'Liberia', 'Saint Helena', 'Burkina Faso', 'Gambia', 'Mali', 'Ghana', 'Mauritania', 'Senegal', 'Cape Verde', 'Cote Divoire', 'Guinea', 'Niger', 'Sierra Leone', 'Guinea-Bissau', 'Nigeria', 'Togo', 'Algeria', 'Egypt', 'Libyan ', 'Morocco', 'Tunisia', 'Sahara', 'Sudan']
    america=['Anguilla', 'Antigua and Barbuda', 'Argentina', 'Aruba', 'Bahamas', 'Bajo Nuevo Bank', 'Barbados', 'Belize', 'Bermuda', 'Bolivia', 'Bonaire', 'Brazil', 'British Virgin Islands', 'Canada', ' Cayman Islands', 'Chile', ' Clipperton Island', 'Colombia', ' Costa Rica', 'Cuba', 'Curaçao', 'Dominica', ' Dominican Republic', 'Ecuador', ' El Salvador', ' Falkland Islands', ' Federal Dependencies of Venezuela', ' French Guiana', 'Greenland', 'Grenada', 'Guadeloupe ', 'Guatemala', 'Guyana', 'Haiti', 'Honduras', 'Jamaica', 'Martinique', 'Mexico', 'Montserrat', 'Navassa Island', 'Nicaragua', 'Panama', 'Paraguay', 'Peru', ' Puerto Rico', 'Saba', ' Saint Barthélemy', 'Saint Kitts and Nevis', ' Saint Lucia', ' Saint Martin', ' Saint Pierre and Miquelon', ' Saint Vincent and the Grenadines', 'Serranilla Bank', ' Sint Eustatius', ' Sint Maarten', 'South Georgia', 'South Sandwich Islands', 'Suriname', ' Trinidad and Tobago', 'Turks and Caicos Islands', 'United States of America', 'USA', 'U.S.A.', ' U.S. Virgin Islands', 'Uruguay', 'Venezuela']
    oceania=['Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia', 'Nauru', 'New Zealand', 'Palau', 'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu']

    if pais in asia:
        return "Asia"
    elif pais in europe:
        return "Europe"
    elif pais in africa:
        return "Africa"
    elif pais in america:
        return "America"
    elif pais in oceania:
        return "Oceania"
    else:
        return "Other"
    



#FUNCION PARA DEVOLVER GRUPOS DE EDAD CUANDO LE DAMOS EDADES SUELTAS EN UN DF
    
#create a function that encapsulates ages in groups

def grupedad(edad):
    if edad <18:
        return "0-18"
    elif edad <=40:
        return "19-40"
    elif edad <=60:
        return "41-60"
    elif edad <=80:
        return "61-80"
    elif edad >80:
        return ">80"
    else:
        return "not a number"

#FUNCION PARA DEVOLVER GRUPOS DE EDAD CUANDO LE DAMOS EDADES SUELTAS EN UN DF PERO EN CATEGORÍAS STRING
    
#create a function that encapsulates ages in groups by stage of age (string)

def grupedad_cat(edad):
    if edad <12:
        return "Child"
    elif edad <=13:
        return "Teen"
    elif edad <=30:
        return "Early Adult"
    elif edad <=60:
        return "Adult"
    elif edad <=80:
        return "Old"
    elif edad >80:
        return "Very old"
    else:
        return "not a number"
    