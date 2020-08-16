import firebase_admin 
from firebase_admin import credentials
from firebase_admin import firestore

firestore_db = credentials.Certificate({
  "type": "service_account",
  "project_id": "mahayoga-firestore",
  "private_key_id": "a668ac6bc7de83e4eaf74fdfd7f3a416106a72bd",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDLwhjYObxOy6T8\n4qz8SP3X9NiHpOa4O+TB45jkFfxrkg2AB+Pa/Fbyr3/Y5wSKxLcA8JtBPAGpIsA/\nqbD9JwPesFZ5OHjvQdF4ubDZH+L1ZttHfLlFGYM+8VFIyJfJ7T1ekW43gpIob9Jh\nkqNx/YnsdMhEH7CNhIjb61ohnfqPfl+E2/lwWdUCp2e/tjcxBPXiABp+eZ4ycT5j\nIJJX7FjJUFSuEnSckLgUTzKOfOjWOmE6ESCcUI+LcRmqgdcUle3r+MZAsU6IN3GT\nGYzTRCC1hyM4cL8ySiHeibnbEbVxrRJPzY9VbkmpotZwq77Q0lCOGR5AHVr7MNgh\ngChG53fZAgMBAAECggEACVWcrRiFWkLADd8V4lThtClWW23K2A5+XgI0OIwSopxF\nRrlAegFsu59zRuzbwL5e998N7cDMVALwiw9rY/LhSCwMj28ZMzTGXjZ7izwyZIr6\nvrKltixYs+Mllc+tYdB0KvHp+lxen8BHrgqkDDkmPrvhiiVoLC4x1YlZpAfzDkG8\nkVi67PcXxwxNyXOq8HOpDUTirs25pX560vViuXRG9+LknTmAQlp7Q3ySpkbZkj/O\n92v3K4x4lz7ISz1IMCl94VOVGNV4WfIH6CJD7V7jOGqKtfhXLihc1D0OYVHYnLEq\n/GPLQJCDhzMNlIE6MJOF3tv2rEhiZQ/5RNDYlMqktQKBgQDoQ6CZ1kdzHuQ9cmcf\nLgO3j8oOCQO7zI517Sw1aRNf4zchXwvZ7vVqlDSErrla40M+hyyYzw4ccn5XO4Rd\nFmV6Pu9ZWucTxk26lSsLuIkcY8zb0mlaE2q3lucu3a8+/BnaJe3IPpC0ouq1Qfpr\n73XDNFQkt9LczWFDC93oaOOxOwKBgQDglLYbNxqIeaejWFrbEGXCPDezhf70kdDo\nHUJLsb1IAz4/uB8tPHN1dwXkD1Qm4Zhp9l+FMy8q1/iuplYPmUKqvti68DN2Lntr\nmhG+KICzX/zOBRq1mT3OjzZQlAg6RY9hpBvknjRKcSsPV6pqLMpdy8HU0XH4eHkt\nuvwzZG7p+wKBgQCx0xUisuwBN6WHZg+Nz60I3Q3VsREqt3Ja1zsBqXEr+Mo8wohQ\nUqOS9eU/sIY5D8ZsGRIL7HrhTMduAiNVIdCPx594yiAhA7J/J7XNQ3u2QLKXmoEO\ndc8+wEo/l3qUvm8Mlf13Um933UPVgq439R40VdwWQKcwZg4RRwSe669oAQKBgHz2\n4toD8HSuVPSUboHk/up0vX3cesC1/quZ1FDwRuWyQEoOdvKh55EeOJ3tVaMI9tlH\naWFh2MYbRNpR3iNx4WHHLivfCpOhS7XVFjhcqzikmbQ9rN4NthGhKNTveiCKojzv\np0GwMmKV1CMGYeIQqE5G2cVFAgkDaFJk8H7cTMdPAoGBANFlWd3QRwjkLtS2fK/O\n9E7Ez6YpNRFOwq1ANEvGDQSs00uay+YWysh4O+DsRQed9XTlSzXFjZvwoSYrbM1a\nB61AAxVXsO3GryS64ztfIL0kJ4oUJsw0ndY/kdz054lodG2SVBQVWnviguFFEbuf\nnpWRC5lm0JAL6f/fupuXhWWC\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-tge6n@mahayoga-firestore.iam.gserviceaccount.com",
  "client_id": "117217282666552167058",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-tge6n%40mahayoga-firestore.iam.gserviceaccount.com"
})
firebase_admin.initialize_app(firestore_db)

db = firestore.client()
doc_ref = db.collection('quotes').stream()
update_ref = db.collection('quotes')

data_len = 1

def monthAsStr(m):
    if m == "01" :
        return "Jan"

    elif m == "02":
        return "Feb"

    elif m == "03":
        return "Mar"

    elif m == "04":
        return "Apr"

    elif m == "05":
        return "May"

    elif m == "06":
        return "Jun"

    elif m == "07":
        return "Jul"

    elif m == "08":
        return "Aug"

    elif m == "09":
        return "Sep"

    elif m == "10":
        return "Oct"

    elif m == "11":
        return "Nov"
    
    elif m == "12":
        return "Dec"

def updateData(doc_id, month, day):
    update_ref.document(doc_id).update({
        'queryParam' : int(month + day),
        'date' : day + " " + monthAsStr(month)
    })

for doc in doc_ref:
    print(data_len)
    if doc.id.find("-") == 1:
        dat = "0" + doc.id
        if len(dat[3:]) == 1:
            updateData(doc.id, "0" + dat[3:], dat[:2])
            #print(doc.id + " : " + "0" + dat[3:] + dat[:2])
        else:
            updateData(doc.id, dat[3:], dat[:2])
            #print(doc.id + " : " +  dat[3:] + dat[:2])

    else:
        dat = doc.id
        if len(dat[3:]) == 1:
            updateData(doc.id, "0" + dat[3:], dat[:2])
            #print(doc.id + " : " + "0" + dat[3:] + dat[:2])
        else:
            updateData(doc.id, dat[3:], dat[:2])
            #print(doc.id + " : " + dat[3:] + dat[:2])

    data_len = data_len + 1
    
    
