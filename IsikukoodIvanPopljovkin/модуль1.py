def Kontroll(isikukood:str):
    """Isikukoodi kontroll number
    On vaja isikukood sisestada
    :param str ik: Inimese isikukood
    :rtype: var Märamata tüüp
    """
    ik_list=list(isikukood)
    s=0
    for i in range(0,10):
        s+=(i%9+1)*int(ik_list[i])
        print(f"{i%9+1}*{int(ik_list[i])}+", end="")
    print(s)
    s=s-(s//11)*11
    print(s)
    if s==int(ik_list[10]):
        vastus=s
    else:
        vastus="Kontroll number on vale"
    return vastus
def Haigla(ik3:int):
    """Haigla 3 isikukoodi numbri alusel
    :param int ik3:
    :rtype: str Haigla ja koht
    """
    if ik3 in range(1,11):
        haigla='Kuresaare'
    elif ik3 in range(11,20):
        haigla='Tartu'
    elif ik3 in range(21,221):
        haigla='Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla'
    elif ik3 in range(221,271):
        haigla=' Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)'
    elif ik3 in range(271,371):
        haigla=' Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla'
    elif ik3 in range(371,421):
        haigla='Narva Haigla'
    elif ik3 in range(421,471):
        haigla='Pärnu Haigla'
    elif ik3 in range(471,491):
        haigla='Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla'
    elif ik3 in range(491,520):
        haigla='Järvamaa Haigla (Paide)' 
    elif ik3 in range(521,571):
        haigla='Rakvere, Tapa haigla'
    elif ik3 in range(571,601):
        haigla='Valga Haigla'
    elif ik3 in range(601,651):
        haigla='Viljandi Haigla'
    else:
        haigla='Viljandi Haigla' 
    return haigla
def Sugu(ik1:int)->str:
    """
    Sugu 1 number
    :param int ik1
    :rtype: str Sugu
    """
    if ik1%2==0:
        sugu="naine"
    else:
        sugu="mees"
    return sugu
