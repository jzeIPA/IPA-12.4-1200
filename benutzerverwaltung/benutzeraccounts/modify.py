from ldap3 import Server, Connection, ALL, MODIFY_REPLACE
from default import settings

#Das Zürckschreiben der LDAP-Verweis funktioniert nicht in Django, daher wird die Python-Operation Modify_Replace erstellt.
#Diese wird als Workaround für die Weiterentwicklung angewendet.

def modify(self,dn,changes,controls=None):
    # Server definieren
    s = Server('192.168.1.12', get_info=ALL)

    # Verbindung definieren
    c = Connection(s, 'cn=ldap_ipa,cn=Users,dc=sbvg,dc=ch', 'Roht4kol', auto_bind=False)
    c.bind()

    # Modify_Replace Operator ausfuehren
    c.modify('cn=ldap_ipa,cn=Users,dc=sbvg,dc=ch',
            {'givenName': [(MODIFY_REPLACE, ['Jusuf'])],
            'sn': [(MODIFY_REPLACE, ['Zera'])]})
    print(c.result)

    # Verbindung trennen
    c.unbind()
