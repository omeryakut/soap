client = zeep.Client(wsdl=wsdl + "/egm_test.wsdl", plugins=[history], wsse=UsernameToken(username=username,password=password, use_digest=True))

        inputDict = {
                     "AsbisTescilReferansNumarasi" : asbisTescilRefNo,
                     "KurumKodu" : kurumKodu,
                     "Plaka" : plaka,
                     "TescilBelgeSeriNo" : tescilBelgeSeriNo,
                     "UserId" : userId 
                     }

        service = client.create_service(binding_name=binding_name, address='http://10.1.3.17:9090/EGMENDPOINT/EGMTest/Router.svc/BankalarToEGMRehin')
        service.PlakaDanAracBul(inputDict)


https://stackoverflow.com/questions/49783252/how-to-change-endpoint-address-in-soap-requests-with-zeep
https://stackoverflow.com/questions/42236251/change-service-url-in-python-zeep        



<soap:Envelope xmlns:egm="http://schemas.datacontract.org/2004/07/EGM.ASBIS.Servisler.BankaServisleri" xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tem="http://tempuri.org/">
    <soap:Header xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">
        <wsse:Security soap:mustUnderstand="true" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
            <wsse:UsernameToken wsu:Id="UsernameToken-6B36D701BAFB065CBC15627557818394">
                <wsse:Username>*****</wsse:Username>
                <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">*****</wsse:Password>
                <wsse:Nonce EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary">BSDn9OHoxi38xbTAJ4Nwvg==</wsse:Nonce>
                <wsu:Created>2019-07-10T10:49:41.839Z</wsu:Created>
            </wsse:UsernameToken>
        </wsse:Security>
        <wsa:Action soap:mustUnderstand="1">http://tempuri.org/IAsbisBankaServis/PlakaDanAracBul</wsa:Action>
        <wsa:To soap:mustUnderstand="1">https://egmtest.egm.gov.tr/EGMTest/Router.svc/BankalarToEGMRehin</wsa:To>
    </soap:Header>
    <soap:Body>
        <tem:PlakaDanAracBul>
            <!--Optional:-->
            <tem:pPlakaDanAracBulRequest>
                <egm:AsbisTescilReferansNumarasi>0</egm:AsbisTescilReferansNumarasi>
                <egm:KurumKodu>131</egm:KurumKodu>
                <egm:Plaka>06BG0952</egm:Plaka>
                <egm:TescilBelgeSerino>AI631776</egm:TescilBelgeSerino>
                <egm:UserId>*****</egm:UserId>
            </tem:pPlakaDanAracBulRequest>
        </tem:PlakaDanAracBul>
    </soap:Body>
</soap:Envelope>




from zeep import Client
from zeep import xsd

client = Client('http://my-endpoint.com/production.svc?wsdl')
service = client.create_service(
    '{http://my-target-namespace-here}myBinding',
    'http://my-endpoint.com/acceptance/')

service.submit('something')



