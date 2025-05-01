
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" >
<head><title>
	Yönlendirme Yapılıyor
</title><meta http-equiv="X-UA-Compatible" content="IE=edge" /><meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport" /><link href="./proliz_boots4/bootstrap/css/bootstrap.min.css" rel="stylesheet" />
<script type="text/javascript">
validNavigation = false;function countdown()  { seconds = document.getElementById("lblKalanSure").innerHTML;              if (seconds > 1) { document.getElementById("lblKalanSure").innerHTML = seconds - 1; setTimeout("countdown()", 1000); } else { prolizMainPageRedirect('login.aspx');                   }              }  setTimeout("countdown()", 1000);
</script>    
<style>
#container { position: relative}
#nested {position: absolute;top: -8px;left: -8px;font-size: 200%;color: rgba(217, 83, 79, 0.7);}
</style>
<link href="../App_Themes/oibs18/oibs18.css" type="text/css" rel="stylesheet" /><link rel="stylesheet" type="text/css" href="/oibs/proliz_boots4/jquery-ui/jquery-ui.min.css"></link><link rel="stylesheet" type="text/css" href="/oibs/proliz_boots4/fontawesome/css/all.min.css"></link><link rel="stylesheet" type="text/css" href="/oibs/proliz_boots4/select2/css/select2.min.css"></link></head>
<body>
<form method="post" action="./redirect.aspx" id="form1">
<div class="aspNetHidden">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="JBarSYVc/kXwbe1706tZ9jpDHG4nFXsIk0BhiEzFQww14SaKg/8wGKNTGqgMMDpEAaB1Cd4aTKl1W7SNFVQwtqiOYE+Oi6Q6rft/XpYdG6OnGt7H9jJzPZ71PlTWuPZX0THWv16m7qb/NbLKxCeCuEz2Zncc9nRTWTRXZw3SzT17QuwFeAgZAO5zE7JidSDEI+Huo3AONbyOMgit2Y36qV7e13OP5gDdGHvE30O1OuVsMzcZ7upHfq6bosacgnQDokpkBcNjshexVNXfcy6Ue+taHuooMa0ETm4KNVS0ikTLJpBYe8fEHax604sSvgwWzZf2YQ==" />
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['form1'];
if (!theForm) {
    theForm = document.form1;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<script src="/oibs/WebResource.axd?d=pynGkmcFUV13He1Qd6_TZBLPcBoAOtY9pdpxwZkxhB0R9Kd8auV1GsRoODb4l9AQFsOyOw2&amp;t=638286173964787378" type="text/javascript"></script>


<script src="/oibs/proliz_boots4/jquery/jquery-3.7.1.min.js" type="text/javascript"></script>
<script src="/oibs/proliz_boots4/jquery-ui/jquery-ui.min.js" type="text/javascript"></script>
<script src="/oibs/proliz_boots4/sweetalert2/sweetalert.min.js" type="text/javascript"></script>
<script src="/oibs/proliz_boots4/select2/js/select2.min.js" type="text/javascript"></script>
<script src="/oibs/utils/ModalPopupWindow_v22_min.js" type="text/javascript"></script><script type="text/javascript">var baseUrl = '/oibs/';var modalWin = new CreateModalPopUpObject();</script>
<script type="text/javascript">
//<![CDATA[
if(window.top.document.getElementById('hidTimerBase')){ window.top.extendTime();}//]]>
</script>

<div class="aspNetHidden">

	<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="65E74D7E" />
	<input type="hidden" name="__SCROLLPOSITIONX" id="__SCROLLPOSITIONX" value="0" />
	<input type="hidden" name="__SCROLLPOSITIONY" id="__SCROLLPOSITIONY" value="0" />
	<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
	<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
	<input type="hidden" name="__VIEWSTATEENCRYPTED" id="__VIEWSTATEENCRYPTED" value="" />
</div>
<div style="text-align: center">
<div class="panel panel-default" style="text-align:center !important;">
<div class="panel-heading"><span id="Label1" style="font-size:12pt;">Oturum Sonlandı</span></div>
<br />
<i class="fal fa-business-time" id="container" style="padding-left:25px;padding-top:25px; color:dimgray; font-size:5.2em"><i class="fal fa-ban" id="nested" style="font-size:1.9em"></i></i>
<br /><br />
<span id="lblIcerik" style="font-size:12pt;"><font color=red><br>Oturum zaman aşımına uğradı.<br>Sisteme tekrar giriş yapılması için yönlendirme yapılıyor.</font></span>
<br /><br />
<span id="lblKalanSure" style="color:#CC3300;font-size:12pt;">2</span>
&nbsp;&nbsp;<span id="Label2" style="font-size:12pt;">sn içerisinde yönlendirme yapılacak</span>
<br /><br /></div></div><div id="myDiv2"><input name="__RequestVerificationToken" type="hidden" value="Vj7_Ma2y72GutaD1XnX1piiJOPNV5dDlXn2euRn-KMygWtY7BPEHB9GNyu8L2b4rPq-9GdFyxfwBqspQalseAq0ZvSg1" /></div>

<script type="text/javascript">
//<![CDATA[

theForm.oldSubmit = theForm.submit;
theForm.submit = WebForm_SaveScrollPositionSubmit;

theForm.oldOnSubmit = theForm.onsubmit;
theForm.onsubmit = WebForm_SaveScrollPositionOnSubmit;
//]]>
</script>
</form>
</body>
</html>
