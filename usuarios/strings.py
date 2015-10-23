# -*- encoding: utf-8 -*-

def crear_cuenta(nombre,url):
    cadena ="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>*|MC:SUBJECT|*</title>
        <style type="text/css">#bodyCell,#bodyTable,body{height:100%%;margin:0;padding:0;width:100%%}table{border-collapse:collapse}a img,img{border:0;outline:0;text-decoration:none}h1,h2,h3,h4,h5,h6{margin:0;padding:0}p{margin:1em 0;padding:0}a{word-wrap:break-word}.ExternalClass,.ReadMsgBody{width:100%%}.ExternalClass,.ExternalClass div,.ExternalClass font,.ExternalClass p,.ExternalClass span,.ExternalClass td{line-height:100%%}table,td{mso-table-lspace:0;mso-table-rspace:0}#outlook a{padding:0}img{-ms-interpolation-mode:bicubic}a,blockquote,body,li,p,table,td{-ms-text-size-adjust:100%%;-webkit-text-size-adjust:100%%}#bodyCell{padding:20px}.mcnImage{vertical-align:bottom}.mcnTextContent img{height:auto}#bodyTable,body{background-color:#f2f2f2}#bodyCell{border-top:0}#templateContainer{border:0}h1{color:#606060;font-size:24px;letter-spacing:-1px}h1,h2{display:block;font-family:Helvetica;font-style:normal;font-weight:700;line-height:125%%;margin:0;text-align:left}h2{color:#404040;font-size:26px;letter-spacing:-.75px}h3{color:#606060;font-size:18px;letter-spacing:-.5px}h3,h4{display:block;font-family:Helvetica;font-style:normal;font-weight:700;line-height:125%%;margin:0;text-align:left}h4{color:gray;font-size:1pc;letter-spacing:normal}#templatePreheader{background-color:#fff;border-top:0;border-bottom:0}.preheaderContainer .mcnTextContent,.preheaderContainer .mcnTextContent p{color:#606060;font-family:Helvetica;font-size:11px;line-height:125%%;text-align:left}.preheaderContainer .mcnTextContent a{color:#606060;font-weight:400;text-decoration:underline}#templateHeader{background-color:#fff;border-top:0;border-bottom:0}.headerContainer .mcnTextContent,.headerContainer .mcnTextContent p{color:#606060;font-family:Helvetica;font-size:15px;line-height:150%%;text-align:left}.headerContainer .mcnTextContent a{color:#6dc6dd;font-weight:400;text-decoration:underline}#templateBody{background-color:#fff;border-top:0;border-bottom:0}.bodyContainer .mcnTextContent,.bodyContainer .mcnTextContent p{color:#606060;font-family:Helvetica;font-size:15px;line-height:150%%;text-align:left}.bodyContainer .mcnTextContent a{color:#6dc6dd;font-weight:400;text-decoration:underline}#templateFooter{background-color:#fff;border-top:0;border-bottom:0}.footerContainer .mcnTextContent,.footerContainer .mcnTextContent p{color:#606060;font-family:Helvetica;font-size:11px;line-height:125%%;text-align:left}.footerContainer .mcnTextContent a{color:#606060;font-weight:400;text-decoration:underline}@media only screen and (max-width:480px){a,blockquote,body,li,p,table,td{-webkit-text-size-adjust:none}}@media only screen and (max-width:480px){body{width:100%%;min-width:100%%}}@media only screen and (max-width:480px){td[id=bodyCell]{padding:10px}}@media only screen and (max-width:480px){table[class=mcnBoxedTextContentContainer],table[class=mcnTextContentContainer]{width:100%%}}@media only screen and (max-width:480px){table[class=mcpreview-image-uploader]{width:100%%;display:none}}@media only screen and (max-width:480px){img[class=mcnImage],table[class=mcnImageGroupContentContainer]{width:100%%}}@media only screen and (max-width:480px){td[class=mcnImageGroupContent]{padding:9px}}@media only screen and (max-width:480px){td[class=mcnImageGroupBlockInner]{padding-bottom:0;padding-top:0}}@media only screen and (max-width:480px){tbody[class=mcnImageGroupBlockOuter]{padding-bottom:9px;padding-top:9px}}@media only screen and (max-width:480px){table[class=mcnCaptionBottomContent],table[class=mcnCaptionLeftImageContentContainer],table[class=mcnCaptionLeftTextContentContainer],table[class=mcnCaptionRightImageContentContainer],table[class=mcnCaptionRightTextContentContainer],table[class=mcnCaptionTopContent],table[class=mcnImageCardLeftTextContentContainer],table[class=mcnImageCardRightTextContentContainer]{width:100%%}}@media only screen and (max-width:480px){td[class=mcnImageCardLeftImageContent],td[class=mcnImageCardRightImageContent]{padding-right:18px;padding-left:18px;padding-bottom:0}}@media only screen and (max-width:480px){td[class=mcnImageCardBottomImageContent]{padding-bottom:9px}}@media only screen and (max-width:480px){td[class=mcnImageCardTopImageContent]{padding-top:18px}}@media only screen and (max-width:480px){table[class=mcnCaptionLeftContentOuter] td[class=mcnTextContent],table[class=mcnCaptionRightContentOuter] td[class=mcnTextContent]{padding-top:9px}}@media only screen and (max-width:480px){td[class=mcnCaptionBlockInner] table[class=mcnCaptionTopContent]:last-child td[class=mcnTextContent]{padding-top:18px}}@media only screen and (max-width:480px){td[class=mcnBoxedTextContentColumn],td[class=mcnTextContent]{padding-left:18px;padding-right:18px}}@media only screen and (max-width:480px){table[id=templateBody],table[id=templateContainer],table[id=templateFooter],table[id=templateHeader],table[id=templatePreheader]{max-width:600px;width:100%%}}@media only screen and (max-width:480px){h1{font-size:24px }}@media only screen and (max-width:480px){h1,h2{line-height:125%%}h2{font-size:20px }}@media only screen and (max-width:480px){h3{font-size:18px }}@media only screen and (max-width:480px){h3,h4{line-height:125%%}h4{font-size:1pc }}@media only screen and (max-width:480px){table[class=mcnBoxedTextContentContainer] td[class=mcnTextContent],td[class=mcnBoxedTextContentContainer] td[class=mcnTextContent] p{font-size:18px ;line-height:125%%}}@media only screen and (max-width:480px){table[id=templatePreheader]{display:block}}@media only screen and (max-width:480px){td[class=preheaderContainer] td[class=mcnTextContent],td[class=preheaderContainer] td[class=mcnTextContent] p{font-size:14px ;line-height:115%%}}@media only screen and (max-width:480px){td[class=bodyContainer] td[class=mcnTextContent],td[class=bodyContainer] td[class=mcnTextContent] p,td[class=headerContainer] td[class=mcnTextContent],td[class=headerContainer] td[class=mcnTextContent] p{font-size:18px ;line-height:125%%}}@media only screen and (max-width:480px){td[class=footerContainer] td[class=mcnTextContent],td[class=footerContainer] td[class=mcnTextContent] p{font-size:14px ;line-height:115%%}}@media only screen and (max-width:480px){td[class=footerContainer] a[class=utilityLink]{display:block}}</style>
    </head>
    <body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0" style="margin: 0;padding: 0;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;background-color: #F2F2F2;height: 100%%   ;width: 100%%   ;">
        <center>
            <table align="center" border="0" cellpadding="0" cellspacing="0" height="100%% " width="100%% " id="bodyTable" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;margin: 0;padding: 0;background-color: #F2F2F2;height: 100%%   ;width: 100%%   ;">
                <tr>
                    <td align="center" valign="top" id="bodyCell" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;margin: 0;padding: 20px;border-top: 0;height: 100%%   ;width: 100%%   ;">
                    <table border="0" cellpadding="0" cellspacing="0" width="600" id="templateContainer" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;border: 0;">
                        <tr>
                            <td align="center" valign="top" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                            <table border="0" cellpadding="0" cellspacing="0" width="600" id="templatePreheader" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;background-color: #FFFFFF;border-top: 0;border-bottom: 0;">
                                <tr>
                                    <td valign="top" class="preheaderContainer" style="padding-top: 9px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%% " class="mcnTextBlock" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                        <tbody class="mcnTextBlockOuter">
                                            <tr>
                                                <td valign="top" class="mcnTextBlockInner" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                <table align="left" border="0" cellpadding="0" cellspacing="0" width="366" class="mcnTextContentContainer" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                    <tbody>
                                                        <tr>
                                                            <td valign="top" class="mcnTextContent" style="padding-top: 9px;padding-left: 18px;padding-bottom: 9px;padding-right: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;color: #606060;font-family: Helvetica;font-size: 11px;line-height: 125%%  ;text-align: left;"> </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                                <table align="right" border="0" cellpadding="0" cellspacing="0" width="197" class="mcnTextContentContainer" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                    <tbody>
                                                        <tr>

                                                            <td valign="top" class="mcnTextContent" style="padding-top: 9px;padding-right: 18px;padding-bottom: 9px;padding-left: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;color: #606060;font-family: Helvetica;font-size: 11px;line-height: 125%%  ;text-align: left;"></td>
                                                        </tr>
                                                    </tbody>
                                                </table></td>
                                            </tr>
                                        </tbody>
                                    </table></td>
                                </tr>
                            </table></td>
                        </tr>
                        <tr>
                            <td align="center" valign="top" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                            <table border="0" cellpadding="0" cellspacing="0" width="600" id="templateHeader" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;background-color: #FFFFFF;border-top: 0;border-bottom: 0;">
                                <tr>
                                    <td valign="top" class="headerContainer" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%% " class="mcnImageBlock" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                        <tbody class="mcnImageBlockOuter">
                                            <tr>
                                                <td valign="top" style="padding: 9px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;" class="mcnImageBlockInner">
                                                <table align="left" width="100%% " border="0" cellpadding="0" cellspacing="0" class="mcnImageContentContainer" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                    <tbody>
                                                        <tr>
                                                            <td class="mcnImageContent" valign="top" style="padding-right: 9px;padding-left: 9px;padding-top: 0;padding-bottom: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;"></td>
                                                        </tr>
                                                    </tbody>
                                                </table></td>
                                            </tr>
                                        </tbody>
                                    </table></td>
                                </tr>
                            </table></td>
                        </tr>
                        <tr>
                            <td align="center" valign="top" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                            <table border="0" cellpadding="0" cellspacing="0" width="600" id="templateBody" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;background-color: #FFFFFF;border-top: 0;border-bottom: 0;">
                                <tr>
                                    <td valign="top" class="bodyContainer" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%% " class="mcnTextBlock" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                        <tbody class="mcnTextBlockOuter">
                                            <tr>
                                                <td valign="top" class="mcnTextBlockInner" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                <table align="left" border="0" cellpadding="0" cellspacing="0" width="600" class="mcnTextContentContainer" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                    <tbody>
                                                        <tr>
                                                            <td valign="top" class="mcnTextContent" style="padding-top: 9px;padding-right: 18px;padding-bottom: 9px;padding-left: 18px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;color: #606060;font-family: Helvetica;font-size: 15px;line-height: 150%%  ;text-align: left;"><h1 style="margin: 0;padding: 0;display: block;font-family: Helvetica;font-size: 24px;font-style: normal;font-weight: bold;line-height: 125%%  ;letter-spacing: -1px;text-align: left;color: #606060  ;">Apreciado(a) %s :</h1><h3 style="margin: 0;padding: 0;display: block;font-family: Helvetica;font-size: 18px;font-style: normal;font-weight: bold;line-height: 125%%  ;letter-spacing: -.5px;text-align: left;color: #606060  ;">&nbsp;</h3>
                                                            <p style="text-align: justify;margin: 1em 0;padding: 0;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;color: #606060;font-family: Helvetica;font-size: 15px;line-height: 150%%  ;">
                                                                El equipo de GoAnalytics te damos la bienvenida. Para culminar con la creaci&oacute;n de tu cuenta te invitamos a dar click en el bot&oacute;n activar cuenta y completar unos datos adicionales.
                                                                <br>
                                                                &nbsp;
                                                            </p></td>
                                                        </tr>
                                                    </tbody>
                                                </table></td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%% " class="mcnButtonBlock" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                        <tbody class="mcnButtonBlockOuter">
                                            <tr>
                                                <td style="padding-top: 0;padding-right: 18px;padding-bottom: 18px;padding-left: 18px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;" valign="top" align="center" class="mcnButtonBlockInner">
                                                <table border="0" cellpadding="0" cellspacing="0" class="mcnButtonContentContainer" style="border-collapse: separate  ;border: 2px solid #47B1DF;border-radius: 5px;background-color: #47B1DF;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                    <tbody>
                                                        <tr>
                                                            <td align="center" valign="middle" class="mcnButtonContent" style="font-family: Arial;font-size: 16px;padding: 16px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;"><a class="mcnButton " title="Go Encuesta" href="%s" target="_blank" style="font-weight: bold;letter-spacing: normal;line-height: 100%%  ;text-align: center;text-decoration: none;color: #FFFFFF;word-wrap: break-word;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">Activar cuenta</a></td>
                                                        </tr>
                                                    </tbody>
                                                </table></td>
                                            </tr>
                                        </tbody>
                                    </table></td>
                                </tr>
                            </table></td>
                        </tr>
                        <tr>
                            <td align="center" valign="top" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                            <table border="0" cellpadding="0" cellspacing="0" width="600" id="templateFooter" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;background-color: #FFFFFF;border-top: 0;border-bottom: 0;">
                                <tr>
                                    <td valign="top" class="footerContainer" style="padding-bottom: 9px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%% " class="mcnTextBlock" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                        <tbody class="mcnTextBlockOuter">
                                            <tr>
                                                <td valign="top" class="mcnTextBlockInner" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                <table align="left" border="0" cellpadding="0" cellspacing="0" width="600" class="mcnTextContentContainer" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                    <tbody>
                                                        <tr>
                                                            <td valign="top" class="mcnTextContent" style="padding-top: 9px;padding-right: 18px;padding-bottom: 9px;padding-left: 18px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;color: #606060;font-family: Helvetica;font-size: 11px;line-height: 125%%  ;text-align: left;"><em>Copyright  NetWorks Lab, All rights reserved.</em>
                                                            <br>
                                                            <br>
                                                            <br>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table></td>
                                            </tr>
                                        </tbody>
                                    </table></td>
                                </tr>
                            </table></td>
                        </tr>
                    </table></td>
                </tr>
            </table>
        </center>
    </body>
    </html>"""%(nombre,url)
    return str(cadena)


def recuperar_cuenta(nombre,url):
    cadena ="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>*|MC:SUBJECT|*</title>
        <style type="text/css">#bodyCell,#bodyTable,body{height:100%%;margin:0;padding:0;width:100%%}table{border-collapse:collapse}a img,img{border:0;outline:0;text-decoration:none}h1,h2,h3,h4,h5,h6{margin:0;padding:0}p{margin:1em 0;padding:0}a{word-wrap:break-word}.ExternalClass,.ReadMsgBody{width:100%%}.ExternalClass,.ExternalClass div,.ExternalClass font,.ExternalClass p,.ExternalClass span,.ExternalClass td{line-height:100%%}table,td{mso-table-lspace:0;mso-table-rspace:0}#outlook a{padding:0}img{-ms-interpolation-mode:bicubic}a,blockquote,body,li,p,table,td{-ms-text-size-adjust:100%%;-webkit-text-size-adjust:100%%}#bodyCell{padding:20px}.mcnImage{vertical-align:bottom}.mcnTextContent img{height:auto}#bodyTable,body{background-color:#f2f2f2}#bodyCell{border-top:0}#templateContainer{border:0}h1{color:#606060;font-size:24px;letter-spacing:-1px}h1,h2{display:block;font-family:Helvetica;font-style:normal;font-weight:700;line-height:125%%;margin:0;text-align:left}h2{color:#404040;font-size:26px;letter-spacing:-.75px}h3{color:#606060;font-size:18px;letter-spacing:-.5px}h3,h4{display:block;font-family:Helvetica;font-style:normal;font-weight:700;line-height:125%%;margin:0;text-align:left}h4{color:gray;font-size:1pc;letter-spacing:normal}#templatePreheader{background-color:#fff;border-top:0;border-bottom:0}.preheaderContainer .mcnTextContent,.preheaderContainer .mcnTextContent p{color:#606060;font-family:Helvetica;font-size:11px;line-height:125%%;text-align:left}.preheaderContainer .mcnTextContent a{color:#606060;font-weight:400;text-decoration:underline}#templateHeader{background-color:#fff;border-top:0;border-bottom:0}.headerContainer .mcnTextContent,.headerContainer .mcnTextContent p{color:#606060;font-family:Helvetica;font-size:15px;line-height:150%%;text-align:left}.headerContainer .mcnTextContent a{color:#6dc6dd;font-weight:400;text-decoration:underline}#templateBody{background-color:#fff;border-top:0;border-bottom:0}.bodyContainer .mcnTextContent,.bodyContainer .mcnTextContent p{color:#606060;font-family:Helvetica;font-size:15px;line-height:150%%;text-align:left}.bodyContainer .mcnTextContent a{color:#6dc6dd;font-weight:400;text-decoration:underline}#templateFooter{background-color:#fff;border-top:0;border-bottom:0}.footerContainer .mcnTextContent,.footerContainer .mcnTextContent p{color:#606060;font-family:Helvetica;font-size:11px;line-height:125%%;text-align:left}.footerContainer .mcnTextContent a{color:#606060;font-weight:400;text-decoration:underline}@media only screen and (max-width:480px){a,blockquote,body,li,p,table,td{-webkit-text-size-adjust:none}}@media only screen and (max-width:480px){body{width:100%%;min-width:100%%}}@media only screen and (max-width:480px){td[id=bodyCell]{padding:10px}}@media only screen and (max-width:480px){table[class=mcnBoxedTextContentContainer],table[class=mcnTextContentContainer]{width:100%%}}@media only screen and (max-width:480px){table[class=mcpreview-image-uploader]{width:100%%;display:none}}@media only screen and (max-width:480px){img[class=mcnImage],table[class=mcnImageGroupContentContainer]{width:100%%}}@media only screen and (max-width:480px){td[class=mcnImageGroupContent]{padding:9px}}@media only screen and (max-width:480px){td[class=mcnImageGroupBlockInner]{padding-bottom:0;padding-top:0}}@media only screen and (max-width:480px){tbody[class=mcnImageGroupBlockOuter]{padding-bottom:9px;padding-top:9px}}@media only screen and (max-width:480px){table[class=mcnCaptionBottomContent],table[class=mcnCaptionLeftImageContentContainer],table[class=mcnCaptionLeftTextContentContainer],table[class=mcnCaptionRightImageContentContainer],table[class=mcnCaptionRightTextContentContainer],table[class=mcnCaptionTopContent],table[class=mcnImageCardLeftTextContentContainer],table[class=mcnImageCardRightTextContentContainer]{width:100%%}}@media only screen and (max-width:480px){td[class=mcnImageCardLeftImageContent],td[class=mcnImageCardRightImageContent]{padding-right:18px;padding-left:18px;padding-bottom:0}}@media only screen and (max-width:480px){td[class=mcnImageCardBottomImageContent]{padding-bottom:9px}}@media only screen and (max-width:480px){td[class=mcnImageCardTopImageContent]{padding-top:18px}}@media only screen and (max-width:480px){table[class=mcnCaptionLeftContentOuter] td[class=mcnTextContent],table[class=mcnCaptionRightContentOuter] td[class=mcnTextContent]{padding-top:9px}}@media only screen and (max-width:480px){td[class=mcnCaptionBlockInner] table[class=mcnCaptionTopContent]:last-child td[class=mcnTextContent]{padding-top:18px}}@media only screen and (max-width:480px){td[class=mcnBoxedTextContentColumn],td[class=mcnTextContent]{padding-left:18px;padding-right:18px}}@media only screen and (max-width:480px){table[id=templateBody],table[id=templateContainer],table[id=templateFooter],table[id=templateHeader],table[id=templatePreheader]{max-width:600px;width:100%%}}@media only screen and (max-width:480px){h1{font-size:24px }}@media only screen and (max-width:480px){h1,h2{line-height:125%%}h2{font-size:20px }}@media only screen and (max-width:480px){h3{font-size:18px }}@media only screen and (max-width:480px){h3,h4{line-height:125%%}h4{font-size:1pc }}@media only screen and (max-width:480px){table[class=mcnBoxedTextContentContainer] td[class=mcnTextContent],td[class=mcnBoxedTextContentContainer] td[class=mcnTextContent] p{font-size:18px ;line-height:125%%}}@media only screen and (max-width:480px){table[id=templatePreheader]{display:block}}@media only screen and (max-width:480px){td[class=preheaderContainer] td[class=mcnTextContent],td[class=preheaderContainer] td[class=mcnTextContent] p{font-size:14px ;line-height:115%%}}@media only screen and (max-width:480px){td[class=bodyContainer] td[class=mcnTextContent],td[class=bodyContainer] td[class=mcnTextContent] p,td[class=headerContainer] td[class=mcnTextContent],td[class=headerContainer] td[class=mcnTextContent] p{font-size:18px ;line-height:125%%}}@media only screen and (max-width:480px){td[class=footerContainer] td[class=mcnTextContent],td[class=footerContainer] td[class=mcnTextContent] p{font-size:14px ;line-height:115%%}}@media only screen and (max-width:480px){td[class=footerContainer] a[class=utilityLink]{display:block}}</style>
    </head>
    <body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0" style="margin: 0;padding: 0;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;background-color: #F2F2F2;height: 100%%   ;width: 100%%   ;">
        <center>
            <table align="center" border="0" cellpadding="0" cellspacing="0" height="100%% " width="100%% " id="bodyTable" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;margin: 0;padding: 0;background-color: #F2F2F2;height: 100%%   ;width: 100%%   ;">
                <tr>
                    <td align="center" valign="top" id="bodyCell" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;margin: 0;padding: 20px;border-top: 0;height: 100%%   ;width: 100%%   ;">
                    <table border="0" cellpadding="0" cellspacing="0" width="600" id="templateContainer" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;border: 0;">
                        <tr>
                            <td align="center" valign="top" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                            <table border="0" cellpadding="0" cellspacing="0" width="600" id="templatePreheader" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;background-color: #FFFFFF;border-top: 0;border-bottom: 0;">
                                <tr>
                                    <td valign="top" class="preheaderContainer" style="padding-top: 9px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%% " class="mcnTextBlock" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                        <tbody class="mcnTextBlockOuter">
                                            <tr>
                                                <td valign="top" class="mcnTextBlockInner" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                <table align="left" border="0" cellpadding="0" cellspacing="0" width="366" class="mcnTextContentContainer" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                    <tbody>
                                                        <tr>

                                                            <td valign="top" class="mcnTextContent" style="padding-top: 9px;padding-left: 18px;padding-bottom: 9px;padding-right: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;color: #606060;font-family: Helvetica;font-size: 11px;line-height: 125%%  ;text-align: left;"> </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                                <table align="right" border="0" cellpadding="0" cellspacing="0" width="197" class="mcnTextContentContainer" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                    <tbody>
                                                        <tr>
                                                            <td valign="top" class="mcnTextContent" style="padding-top: 9px;padding-right: 18px;padding-bottom: 9px;padding-left: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;color: #606060;font-family: Helvetica;font-size: 11px;line-height: 125%%  ;text-align: left;"></td>
                                                        </tr>
                                                    </tbody>
                                                </table></td>
                                            </tr>
                                        </tbody>
                                    </table></td>
                                </tr>
                            </table></td>
                        </tr>
                        <tr>
                            <td align="center" valign="top" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                            <table border="0" cellpadding="0" cellspacing="0" width="600" id="templateHeader" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;background-color: #FFFFFF;border-top: 0;border-bottom: 0;">
                                <tr>
                                    <td valign="top" class="headerContainer" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%% " class="mcnImageBlock" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                        <tbody class="mcnImageBlockOuter">
                                            <tr>
                                                <td valign="top" style="padding: 9px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;" class="mcnImageBlockInner">
                                                <table align="left" width="100%% " border="0" cellpadding="0" cellspacing="0" class="mcnImageContentContainer" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                    <tbody>
                                                        <tr>
                                                            <td class="mcnImageContent" valign="top" style="padding-right: 9px;padding-left: 9px;padding-top: 0;padding-bottom: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;"></td>
                                                        </tr>
                                                    </tbody>
                                                </table></td>
                                            </tr>
                                        </tbody>
                                    </table></td>
                                </tr>
                            </table></td>
                        </tr>
                        <tr>
                            <td align="center" valign="top" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                            <table border="0" cellpadding="0" cellspacing="0" width="600" id="templateBody" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;background-color: #FFFFFF;border-top: 0;border-bottom: 0;">
                                <tr>
                                    <td valign="top" class="bodyContainer" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%% " class="mcnTextBlock" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                        <tbody class="mcnTextBlockOuter">
                                            <tr>
                                                <td valign="top" class="mcnTextBlockInner" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                <table align="left" border="0" cellpadding="0" cellspacing="0" width="600" class="mcnTextContentContainer" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                    <tbody>
                                                        <tr>
                                                            <td valign="top" class="mcnTextContent" style="padding-top: 9px;padding-right: 18px;padding-bottom: 9px;padding-left: 18px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;color: #606060;font-family: Helvetica;font-size: 15px;line-height: 150%%  ;text-align: left;"><h1 style="margin: 0;padding: 0;display: block;font-family: Helvetica;font-size: 24px;font-style: normal;font-weight: bold;line-height: 125%%  ;letter-spacing: -1px;text-align: left;color: #606060  ;">Apreciado(a) %s :</h1><h3 style="margin: 0;padding: 0;display: block;font-family: Helvetica;font-size: 18px;font-style: normal;font-weight: bold;line-height: 125%%  ;letter-spacing: -.5px;text-align: left;color: #606060  ;">&nbsp;</h3>
                                                            <p style="text-align: justify;margin: 1em 0;padding: 0;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;color: #606060;font-family: Helvetica;font-size: 15px;line-height: 150%%  ;">
                                                                Se ha solicitado un cambio de clave en te cuenta de GoAnalytics. Si no ha solicitado este servicio, comun&iacute;quese con su consultor de confianza para tomar las medidas pertinentes. Para continuar con el proceso le invitamos a dar click en el bot&oacute;n continuar.                                                                <br>
                                                                &nbsp;
                                                            </p></td>
                                                        </tr>
                                                    </tbody>
                                                </table></td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%% " class="mcnButtonBlock" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                        <tbody class="mcnButtonBlockOuter">
                                            <tr>
                                                <td style="padding-top: 0;padding-right: 18px;padding-bottom: 18px;padding-left: 18px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;" valign="top" align="center" class="mcnButtonBlockInner">
                                                <table border="0" cellpadding="0" cellspacing="0" class="mcnButtonContentContainer" style="border-collapse: separate  ;border: 2px solid #47B1DF;border-radius: 5px;background-color: #47B1DF;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                    <tbody>
                                                        <tr>
                                                            <td align="center" valign="middle" class="mcnButtonContent" style="font-family: Arial;font-size: 16px;padding: 16px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;"><a class="mcnButton " title="Go Encuesta" href="%s" target="_blank" style="font-weight: bold;letter-spacing: normal;line-height: 100%%  ;text-align: center;text-decoration: none;color: #FFFFFF;word-wrap: break-word;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">Continuar</a></td>
                                                        </tr>
                                                    </tbody>
                                                </table></td>
                                            </tr>
                                        </tbody>
                                    </table></td>
                                </tr>
                            </table></td>
                        </tr>
                        <tr>
                            <td align="center" valign="top" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                            <table border="0" cellpadding="0" cellspacing="0" width="600" id="templateFooter" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;background-color: #FFFFFF;border-top: 0;border-bottom: 0;">
                                <tr>
                                    <td valign="top" class="footerContainer" style="padding-bottom: 9px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%% " class="mcnTextBlock" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                        <tbody class="mcnTextBlockOuter">
                                            <tr>
                                                <td valign="top" class="mcnTextBlockInner" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                <table align="left" border="0" cellpadding="0" cellspacing="0" width="600" class="mcnTextContentContainer" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                    <tbody>
                                                        <tr>
                                                            <td valign="top" class="mcnTextContent" style="padding-top: 9px;padding-right: 18px;padding-bottom: 9px;padding-left: 18px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;color: #606060;font-family: Helvetica;font-size: 11px;line-height: 125%%  ;text-align: left;"><em>Copyright  NetWorks Lab, All rights reserved.</em>
                                                            <br>
                                                            <br>
                                                            <br>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table></td>
                                            </tr>
                                        </tbody>
                                    </table></td>
                                </tr>
                            </table></td>
                        </tr>
                    </table></td>
                </tr>
            </table>
        </center>
    </body>
    </html>"""%(nombre,url)
    return str(cadena)


def correo_standar(urlimg,genero,nombre,titulo,texto_correo,url):
    cadena ="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>*|MC:SUBJECT|*</title>
        <style type="text/css">#bodyCell,#bodyTable,body{height:100%%;margin:0;padding:0;width:100%%}table{border-collapse:collapse}a img,img{border:0;outline:0;text-decoration:none}h1,h2,h3,h4,h5,h6{margin:0;padding:0}p{margin:1em 0;padding:0}a{word-wrap:break-word}.ExternalClass,.ReadMsgBody{width:100%%}.ExternalClass,.ExternalClass div,.ExternalClass font,.ExternalClass p,.ExternalClass span,.ExternalClass td{line-height:100%%}table,td{mso-table-lspace:0;mso-table-rspace:0}#outlook a{padding:0}img{-ms-interpolation-mode:bicubic}a,blockquote,body,li,p,table,td{-ms-text-size-adjust:100%%;-webkit-text-size-adjust:100%%}#bodyCell{padding:20px}.mcnImage{vertical-align:bottom}.mcnTextContent img{height:auto}#bodyTable,body{background-color:#f2f2f2}#bodyCell{border-top:0}#templateContainer{border:0}h1{color:#606060;font-size:24px;letter-spacing:-1px}h1,h2{display:block;font-family:Helvetica;font-style:normal;font-weight:700;line-height:125%%;margin:0;text-align:left}h2{color:#404040;font-size:26px;letter-spacing:-.75px}h3{color:#606060;font-size:18px;letter-spacing:-.5px}h3,h4{display:block;font-family:Helvetica;font-style:normal;font-weight:700;line-height:125%%;margin:0;text-align:left}h4{color:gray;font-size:1pc;letter-spacing:normal}#templatePreheader{background-color:#fff;border-top:0;border-bottom:0}.preheaderContainer .mcnTextContent,.preheaderContainer .mcnTextContent p{color:#606060;font-family:Helvetica;font-size:11px;line-height:125%%;text-align:left}.preheaderContainer .mcnTextContent a{color:#606060;font-weight:400;text-decoration:underline}#templateHeader{background-color:#fff;border-top:0;border-bottom:0}.headerContainer .mcnTextContent,.headerContainer .mcnTextContent p{color:#606060;font-family:Helvetica;font-size:15px;line-height:150%%;text-align:left}.headerContainer .mcnTextContent a{color:#6dc6dd;font-weight:400;text-decoration:underline}#templateBody{background-color:#fff;border-top:0;border-bottom:0}.bodyContainer .mcnTextContent,.bodyContainer .mcnTextContent p{color:#606060;font-family:Helvetica;font-size:15px;line-height:150%%;text-align:left}.bodyContainer .mcnTextContent a{color:#6dc6dd;font-weight:400;text-decoration:underline}#templateFooter{background-color:#fff;border-top:0;border-bottom:0}.footerContainer .mcnTextContent,.footerContainer .mcnTextContent p{color:#606060;font-family:Helvetica;font-size:11px;line-height:125%%;text-align:left}.footerContainer .mcnTextContent a{color:#606060;font-weight:400;text-decoration:underline}@media only screen and (max-width:480px){a,blockquote,body,li,p,table,td{-webkit-text-size-adjust:none}}@media only screen and (max-width:480px){body{width:100%%;min-width:100%%}}@media only screen and (max-width:480px){td[id=bodyCell]{padding:10px}}@media only screen and (max-width:480px){table[class=mcnBoxedTextContentContainer],table[class=mcnTextContentContainer]{width:100%%}}@media only screen and (max-width:480px){table[class=mcpreview-image-uploader]{width:100%%;display:none}}@media only screen and (max-width:480px){img[class=mcnImage],table[class=mcnImageGroupContentContainer]{width:100%%}}@media only screen and (max-width:480px){td[class=mcnImageGroupContent]{padding:9px}}@media only screen and (max-width:480px){td[class=mcnImageGroupBlockInner]{padding-bottom:0;padding-top:0}}@media only screen and (max-width:480px){tbody[class=mcnImageGroupBlockOuter]{padding-bottom:9px;padding-top:9px}}@media only screen and (max-width:480px){table[class=mcnCaptionBottomContent],table[class=mcnCaptionLeftImageContentContainer],table[class=mcnCaptionLeftTextContentContainer],table[class=mcnCaptionRightImageContentContainer],table[class=mcnCaptionRightTextContentContainer],table[class=mcnCaptionTopContent],table[class=mcnImageCardLeftTextContentContainer],table[class=mcnImageCardRightTextContentContainer]{width:100%%}}@media only screen and (max-width:480px){td[class=mcnImageCardLeftImageContent],td[class=mcnImageCardRightImageContent]{padding-right:18px;padding-left:18px;padding-bottom:0}}@media only screen and (max-width:480px){td[class=mcnImageCardBottomImageContent]{padding-bottom:9px}}@media only screen and (max-width:480px){td[class=mcnImageCardTopImageContent]{padding-top:18px}}@media only screen and (max-width:480px){table[class=mcnCaptionLeftContentOuter] td[class=mcnTextContent],table[class=mcnCaptionRightContentOuter] td[class=mcnTextContent]{padding-top:9px}}@media only screen and (max-width:480px){td[class=mcnCaptionBlockInner] table[class=mcnCaptionTopContent]:last-child td[class=mcnTextContent]{padding-top:18px}}@media only screen and (max-width:480px){td[class=mcnBoxedTextContentColumn],td[class=mcnTextContent]{padding-left:18px;padding-right:18px}}@media only screen and (max-width:480px){table[id=templateBody],table[id=templateContainer],table[id=templateFooter],table[id=templateHeader],table[id=templatePreheader]{max-width:600px;width:100%%}}@media only screen and (max-width:480px){h1{font-size:24px }}@media only screen and (max-width:480px){h1,h2{line-height:125%%}h2{font-size:20px }}@media only screen and (max-width:480px){h3{font-size:18px }}@media only screen and (max-width:480px){h3,h4{line-height:125%%}h4{font-size:1pc }}@media only screen and (max-width:480px){table[class=mcnBoxedTextContentContainer] td[class=mcnTextContent],td[class=mcnBoxedTextContentContainer] td[class=mcnTextContent] p{font-size:18px ;line-height:125%%}}@media only screen and (max-width:480px){table[id=templatePreheader]{display:block}}@media only screen and (max-width:480px){td[class=preheaderContainer] td[class=mcnTextContent],td[class=preheaderContainer] td[class=mcnTextContent] p{font-size:14px ;line-height:115%%}}@media only screen and (max-width:480px){td[class=bodyContainer] td[class=mcnTextContent],td[class=bodyContainer] td[class=mcnTextContent] p,td[class=headerContainer] td[class=mcnTextContent],td[class=headerContainer] td[class=mcnTextContent] p{font-size:18px ;line-height:125%%}}@media only screen and (max-width:480px){td[class=footerContainer] td[class=mcnTextContent],td[class=footerContainer] td[class=mcnTextContent] p{font-size:14px ;line-height:115%%}}@media only screen and (max-width:480px){td[class=footerContainer] a[class=utilityLink]{display:block}}</style>
    </head>
    <body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0" style="margin: 0;padding: 0;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;background-color: #F2F2F2;height: 100%%   ;width: 100%%   ;">
        <center>
            <table align="center" border="0" cellpadding="0" cellspacing="0" height="100%% " width="100%% " id="bodyTable" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;margin: 0;padding: 0;background-color: #F2F2F2;height: 100%%   ;width: 100%%   ;">
                <tr>
                    <td align="center" valign="top" id="bodyCell" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;margin: 0;padding: 20px;border-top: 0;height: 100%%   ;width: 100%%   ;">
                    <table border="0" cellpadding="0" cellspacing="0" width="600" id="templateContainer" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;border: 0;">
                        <tr>
                            <td align="center" valign="top" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                            <table border="0" cellpadding="0" cellspacing="0" width="600" id="templatePreheader" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;background-color: #FFFFFF;border-top: 0;border-bottom: 0;">
                                <tr>
                                    <td valign="top" class="preheaderContainer" style="padding-top: 9px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%% " class="mcnTextBlock" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                        <tbody class="mcnTextBlockOuter">
                                            <tr>
                                                <td valign="top" class="mcnTextBlockInner" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                <table align="left" border="0" cellpadding="0" cellspacing="0" width="366" class="mcnTextContentContainer" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                    <tbody>
                                                        <tr>
                                                            <td valign="top" class="mcnTextContent" style="padding-top: 9px;padding-left: 18px;padding-bottom: 9px;padding-right: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;color: #606060;font-family: Helvetica;font-size: 11px;line-height: 125%%  ;text-align: left;"> </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                                <table align="right" border="0" cellpadding="0" cellspacing="0" width="197" class="mcnTextContentContainer" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                    <tbody>
                                                        <tr>
                                                            <td valign="top" class="mcnTextContent" style="padding-top: 9px;padding-right: 18px;padding-bottom: 9px;padding-left: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;color: #606060;font-family: Helvetica;font-size: 11px;line-height: 125%%  ;text-align: left;"></td>
                                                        </tr>
                                                    </tbody>
                                                </table></td>
                                            </tr>
                                        </tbody>
                                    </table></td>
                                </tr>
                            </table></td>
                        </tr>
                        <tr>
                            <td align="center" valign="top" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                            <table border="0" cellpadding="0" cellspacing="0" width="600" id="templateHeader" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;background-color: #FFFFFF;border-top: 0;border-bottom: 0;">
                                <tr>
                                    <td valign="top" class="headerContainer" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%% " class="mcnImageBlock" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                        <tbody class="mcnImageBlockOuter">
                                            <tr>
                                                <td valign="top" style="padding: 9px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;" class="mcnImageBlockInner">
                                                <table align="left" width="100%% " border="0" cellpadding="0" cellspacing="0" class="mcnImageContentContainer" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                    <tbody>
                                                        <tr>
                                                            <td class="mcnImageContent" valign="top" style="padding-right: 9px;padding-left: 9px;padding-top: 0;padding-bottom: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;"><img align="left" alt="" src="%s" width="225" style="margin:0 auto 0 30%%  ;max-width: 225px;padding-bottom: 0;display: inline  ;vertical-align: bottom;border: 0;outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;" class="mcnImage"></td>
                                                        </tr>
                                                    </tbody>
                                                </table></td>
                                            </tr>
                                        </tbody>
                                    </table></td>
                                </tr>
                            </table></td>
                        </tr>
                        <tr>
                            <td align="center" valign="top" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                            <table border="0" cellpadding="0" cellspacing="0" width="600" id="templateBody" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;background-color: #FFFFFF;border-top: 0;border-bottom: 0;">
                                <tr>
                                    <td valign="top" class="bodyContainer" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%% " class="mcnTextBlock" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                        <tbody class="mcnTextBlockOuter">
                                            <tr>
                                                <td valign="top" class="mcnTextBlockInner" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                <table align="left" border="0" cellpadding="0" cellspacing="0" width="600" class="mcnTextContentContainer" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                    <tbody>
                                                        <tr>
                                                            <td valign="top" class="mcnTextContent" style="padding-top: 9px;padding-right: 18px;padding-bottom: 9px;padding-left: 18px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;color: #606060;font-family: Helvetica;font-size: 15px;line-height: 150%%  ;text-align: left;"><h1 style="margin: 0;padding: 0;display: block;font-family: Helvetica;font-size: 24px;font-style: normal;font-weight: bold;line-height: 125%%  ;letter-spacing: -1px;text-align: left;color: #606060  ;">Apreciad%s %s :</h1><h3 style="margin: 0;padding: 0;display: block;font-family: Helvetica;font-size: 18px;font-style: normal;font-weight: bold;line-height: 125%%  ;letter-spacing: -.5px;text-align: left;color: #606060  ;">&nbsp;</h3>
                                                            <p style="text-align: justify;margin: 1em 0;padding: 0;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;color: #606060;font-family: Helvetica;font-size: 15px;line-height: 150%%  ;">
                                                                <br>%s<br><br>
                                                                %s
                                                                <br>
                                                                &nbsp;
                                                            </p></td>
                                                        </tr>
                                                    </tbody>
                                                </table></td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%% " class="mcnButtonBlock" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                        <tbody class="mcnButtonBlockOuter">
                                            <tr>
                                                <td style="padding-top: 0;padding-right: 18px;padding-bottom: 18px;padding-left: 18px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;" valign="top" align="center" class="mcnButtonBlockInner">
                                                <table border="0" cellpadding="0" cellspacing="0" class="mcnButtonContentContainer" style="border-collapse: separate  ;border: 2px solid #47B1DF;border-radius: 5px;background-color: #47B1DF;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                    <tbody>
                                                        <tr>
                                                            <td align="center" valign="middle" class="mcnButtonContent" style="font-family: Arial;font-size: 16px;padding: 16px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;"><a class="mcnButton " title="Go Encuesta" href="%s" target="_blank" style="font-weight: bold;letter-spacing: normal;line-height: 100%%  ;text-align: center;text-decoration: none;color: #FFFFFF;word-wrap: break-word;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">Go Encuesta</a></td>
                                                        </tr>
                                                    </tbody>
                                                </table></td>
                                            </tr>
                                        </tbody>
                                    </table></td>
                                </tr>
                            </table></td>
                        </tr>
                        <tr>
                            <td align="center" valign="top" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                            <table border="0" cellpadding="0" cellspacing="0" width="600" id="templateFooter" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;background-color: #FFFFFF;border-top: 0;border-bottom: 0;">
                                <tr>
                                    <td valign="top" class="footerContainer" style="padding-bottom: 9px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%% " class="mcnTextBlock" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                        <tbody class="mcnTextBlockOuter">
                                            <tr>
                                                <td valign="top" class="mcnTextBlockInner" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                <table align="left" border="0" cellpadding="0" cellspacing="0" width="600" class="mcnTextContentContainer" style="border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;">
                                                    <tbody>
                                                        <tr>
                                                            <td valign="top" class="mcnTextContent" style="padding-top: 9px;padding-right: 18px;padding-bottom: 9px;padding-left: 18px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%%  ;-webkit-text-size-adjust: 100%%  ;color: #606060;font-family: Helvetica;font-size: 11px;line-height: 125%%  ;text-align: left;"><em>Copyright  NetWorks Lab, All rights reserved.</em>
                                                            <br>
                                                            <br>
                                                            <br>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table></td>
                                            </tr>
                                        </tbody>
                                    </table></td>
                                </tr>
                            </table></td>
                        </tr>
                    </table></td>
                </tr>
            </table>
        </center>
    </body>
    </html>"""%(urlimg,genero,nombre,titulo,texto_correo,url)
    return str(cadena)
