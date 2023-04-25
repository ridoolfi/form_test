import smtplib
import email.message
import form_mathv1

def enviar_email():  
    corpo_email = f"""
    <p>{'=-' * 10}</p>
    <p>Nome: {form_mathv1.nome}</p>
    <p>Email: {form_mathv1.email}</p>
    <p>Idade: {form_mathv1.Idade}</p>
    <p>Opinião: {form_mathv1.opn}</p>
    <p>{'=-' * 10}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "O seu formulário foi Preenchido. Confira!"
    msg['From'] = 'formtesteemail@gmail.com'
    msg['To'] = email
    password = 'alltomatic' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
