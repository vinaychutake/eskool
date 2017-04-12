<map version="1.0.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1491812991422" ID="ID_1203633332" MODIFIED="1491822623497" TEXT="New Mindmap">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      CM - client management
    </p>
    <p>
      AM - auth management
    </p>
    <p>
      ACM - Academics management
    </p>
    <p>
      STM - student management
    </p>
    <p>
      SM: Syllabus management
    </p>
    <p>
      TP: Time table planner
    </p>
    <p>
      ATM: Attendance management
    </p>
    <p>
      HM: Home work management
    </p>
    <p>
      EM: Exam management
    </p>
    <p>
      RM: Result management
    </p>
  </body>
</html></richcontent>
<node CREATED="1475205406481" FOLDED="true" HGAP="21" ID="ID_958304365" MODIFIED="1491979964413" POSITION="right" TEXT="cm_institute" VSHIFT="-20">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Table for client (generally coaching class/school).
    </p>
  </body>
</html></richcontent>
<icon BUILTIN="go"/>
<node CREATED="1475205425343" ID="ID_1864710768" MODIFIED="1475811353656" TEXT="id: int, ai, pk"/>
<node CREATED="1475205541841" ID="ID_1101682600" MODIFIED="1475205566005" TEXT="name: varchar(80), not null, unique"/>
<node CREATED="1475205669138" ID="ID_319416483" MODIFIED="1475205681904" TEXT="code: varchar(48), not null, unique"/>
<node CREATED="1475205922222" ID="ID_921517942" MODIFIED="1491813221690" TEXT="sub_domain: varchar(48), not null, unique">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      sub domain for each class
    </p>
    <p>
      
    </p>
    <p>
      e.g.
    </p>
    <p>
      &#160;&#160;school1.xxx.com
    </p>
    <p>
      &#160;&#160;school2.xxx.com
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1475205735641" ID="ID_220300606" MODIFIED="1476363689944" TEXT="logo: varchar(80), not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Logo which will be displayed to all students and teachers on their dashboard
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1475206093199" ID="ID_812691571" MODIFIED="1476517547340" TEXT="type: char(S/A), not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      S: System coaching class
    </p>
    <p>
      A: Application coaching class
    </p>
    <p>
      
    </p>
    <p>
      We need to add System coaching class through initial json and map super user with that coaching class
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1475205618928" ID="ID_1746371491" MODIFIED="1491814613693" TEXT="status: char(1), not null, default A">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      A: Active
    </p>
    <p>
      I: Inactive
    </p>
    <p>
      D: Deleted
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1475206588678" FOLDED="true" ID="ID_1342525024" MODIFIED="1491816006615" POSITION="right" TEXT="am_user">
<icon BUILTIN="go"/>
<node CREATED="1475205425343" ID="ID_506772145" MODIFIED="1491816004507" TEXT="id: int, ai, pk">
<linktarget COLOR="#b0b0b0" DESTINATION="ID_506772145" ENDARROW="Default" ENDINCLINATION="331;0;" ID="Arrow_ID_192768009" SOURCE="ID_1691466592" STARTARROW="None" STARTINCLINATION="331;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_506772145" ENDARROW="Default" ENDINCLINATION="331;0;" ID="Arrow_ID_118058252" SOURCE="ID_589790282" STARTARROW="None" STARTINCLINATION="331;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_506772145" ENDARROW="Default" ENDINCLINATION="651;0;" ID="Arrow_ID_376627978" SOURCE="ID_297229503" STARTARROW="None" STARTINCLINATION="651;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_506772145" ENDARROW="Default" ENDINCLINATION="651;0;" ID="Arrow_ID_1501461064" SOURCE="ID_10372465" STARTARROW="None" STARTINCLINATION="651;0;"/>
</node>
<node CREATED="1475206610448" ID="ID_261830528" MODIFIED="1475725921781" TEXT="username: varchar(48), unique, not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Its available in default djangos user model
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1475206638734" ID="ID_945247522" MODIFIED="1475206729687" TEXT="first_name: varchar(48), not null"/>
<node CREATED="1475206638734" ID="ID_1179728286" MODIFIED="1475206672952" TEXT="middle_name: varchar(48), null"/>
<node CREATED="1475206638734" ID="ID_715756600" MODIFIED="1475206685062" TEXT="last_name: varchar(48), not null"/>
<node CREATED="1475725998864" ID="ID_1515054573" MODIFIED="1475726012904" TEXT="birth_date: datetime, null"/>
<node CREATED="1475726017783" ID="ID_679357928" MODIFIED="1475726027911" TEXT="profile_pic: varchar(48), null"/>
<node CREATED="1475395163016" ID="ID_614193823" MODIFIED="1475395194420" TEXT="is_admin: boolean, default False"/>
<node CREATED="1475206868381" ID="ID_98992872" MODIFIED="1475395196101" TEXT="is_active: boolean, default True"/>
<node CREATED="1475206886094" ID="ID_389554503" MODIFIED="1475206895813" TEXT="is_deleted: boolean, default False"/>
</node>
<node CREATED="1475392400635" FOLDED="true" ID="ID_1216388344" MODIFIED="1491814809743" POSITION="right" TEXT="am_address">
<icon BUILTIN="go"/>
<node CREATED="1475205425343" ID="ID_1244272406" MODIFIED="1475593337716" TEXT="id: int, ai, pk"/>
<node CREATED="1491814736096" ID="ID_1691466592" MODIFIED="1491814755484" TEXT="user: int, fk(am_user: id)">
<arrowlink DESTINATION="ID_506772145" ENDARROW="Default" ENDINCLINATION="331;0;" ID="Arrow_ID_192768009" STARTARROW="None" STARTINCLINATION="331;0;"/>
<arrowlink COLOR="#b0b0b0" DESTINATION="ID_477875372" ENDARROW="Default" ENDINCLINATION="331;0;" ID="Arrow_ID_1526062388" STARTARROW="None" STARTINCLINATION="331;0;"/>
<arrowlink COLOR="#b0b0b0" DESTINATION="ID_1925000247" ENDARROW="Default" ENDINCLINATION="331;0;" ID="Arrow_ID_214256554" STARTARROW="None" STARTINCLINATION="331;0;"/>
</node>
<node CREATED="1475205541841" ID="ID_1419564251" MODIFIED="1475392713458" TEXT="address1: varchar(80), not null"/>
<node CREATED="1475205541841" ID="ID_102608298" MODIFIED="1475394311162" TEXT="address2: varchar(80), not null"/>
<node CREATED="1475205541841" ID="ID_1355196680" MODIFIED="1475394316842" TEXT="address3: varchar(80), not null"/>
<node CREATED="1475205618928" ID="ID_1681426747" MODIFIED="1491814754566" TEXT="status: char(1), not null, default A">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      A: Active
    </p>
    <p>
      I: Inactive
    </p>
    <p>
      D: Deleted
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1475394899918" FOLDED="true" ID="ID_156595343" MODIFIED="1491814809744" POSITION="right" TEXT="am_contact_number">
<icon BUILTIN="go"/>
<node CREATED="1475205425343" ID="ID_1987699903" MODIFIED="1491814599419" TEXT="id: int, ai, pk"/>
<node CREATED="1491814736096" ID="ID_589790282" MODIFIED="1491814766273" TEXT="user: int, fk(am_user: id)">
<arrowlink DESTINATION="ID_506772145" ENDARROW="Default" ENDINCLINATION="331;0;" ID="Arrow_ID_118058252" STARTARROW="None" STARTINCLINATION="331;0;"/>
<arrowlink COLOR="#b0b0b0" DESTINATION="ID_477875372" ENDARROW="Default" ENDINCLINATION="331;0;" ID="Arrow_ID_1269383389" STARTARROW="None" STARTINCLINATION="331;0;"/>
<arrowlink COLOR="#b0b0b0" DESTINATION="ID_1925000247" ENDARROW="Default" ENDINCLINATION="331;0;" ID="Arrow_ID_1114048425" STARTARROW="None" STARTINCLINATION="331;0;"/>
</node>
<node CREATED="1475394999444" ID="ID_1965120377" MODIFIED="1475725220875" TEXT="contact_number: varchar(20), not null"/>
<node CREATED="1475205618928" ID="ID_852607818" MODIFIED="1491814766076" TEXT="status: char(1), not null, default A">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      A: Active
    </p>
    <p>
      I: Inactive
    </p>
    <p>
      D: Deleted
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1479790673602" ID="ID_1496439367" MODIFIED="1491814809744" POSITION="right" TEXT="am_group">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Its djangos group model
    </p>
    <p>
      
    </p>
    <p>
      e.g. - Receptionist, Accoutant
    </p>
  </body>
</html></richcontent>
<icon BUILTIN="go"/>
</node>
<node CREATED="1479790699736" ID="ID_504338868" MODIFIED="1491821007244" POSITION="right" TEXT="am_permission">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Djangos permission model
    </p>
  </body>
</html></richcontent>
<icon BUILTIN="go"/>
</node>
<node CREATED="1479790719159" ID="ID_923548273" MODIFIED="1491821007257" POSITION="right" TEXT="am_group_permission_map">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Djangos group permission map table
    </p>
  </body>
</html></richcontent>
<icon BUILTIN="go"/>
</node>
<node CREATED="1479790761054" ID="ID_1217484472" MODIFIED="1491821007262" POSITION="right" TEXT="am_user_group_map">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      User group map
    </p>
  </body>
</html></richcontent>
<icon BUILTIN="go"/>
</node>
<node CREATED="1475602719211" FOLDED="true" HGAP="36" ID="ID_1517393139" MODIFIED="1491816719179" POSITION="left" TEXT="acm_academic_year" VSHIFT="24">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      e.g. 2015-16, 2014-15, 2013-14
    </p>
  </body>
</html></richcontent>
<icon BUILTIN="go"/>
<node CREATED="1475205425343" ID="ID_1058266612" MODIFIED="1491816622409" TEXT="id: int, ai, pk">
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1058266612" ENDARROW="Default" ENDINCLINATION="466;0;" ID="Arrow_ID_1888153003" SOURCE="ID_311848433" STARTARROW="None" STARTINCLINATION="466;0;"/>
</node>
<node CREATED="1475602832679" ID="ID_1762798482" MODIFIED="1491816346736" TEXT="name: varchar(12), not null, unique"/>
<node CREATED="1475205618928" ID="ID_1495112730" MODIFIED="1475603028833" TEXT="status: char(1), not null, default A">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      A: Active
    </p>
    <p>
      I: Inactive
    </p>
    <p>
      D: Deleted
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1475603312205" FOLDED="true" HGAP="41" ID="ID_1709206610" MODIFIED="1491820464991" POSITION="left" TEXT="acm_subject" VSHIFT="-2">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      e.g. Mathematics, Science, History
    </p>
  </body>
</html></richcontent>
<icon BUILTIN="go"/>
<node CREATED="1475205425343" ID="ID_1485683775" MODIFIED="1491820301638" TEXT="id: int, ai, pk">
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1485683775" ENDARROW="Default" ENDINCLINATION="259;0;" ID="Arrow_ID_755531469" SOURCE="ID_739478321" STARTARROW="None" STARTINCLINATION="259;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1485683775" ENDARROW="Default" ENDINCLINATION="399;0;" ID="Arrow_ID_341975188" SOURCE="ID_806215496" STARTARROW="None" STARTINCLINATION="399;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1485683775" ENDARROW="Default" ENDINCLINATION="497;0;" ID="Arrow_ID_892412924" SOURCE="ID_603658207" STARTARROW="None" STARTINCLINATION="497;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1485683775" ENDARROW="Default" ENDINCLINATION="294;0;" ID="Arrow_ID_795597104" SOURCE="ID_855284857" STARTARROW="None" STARTINCLINATION="294;0;"/>
</node>
<node CREATED="1475602832679" ID="ID_1515599052" MODIFIED="1491816379883" TEXT="name: varchar(80), not null, unique"/>
<node CREATED="1475205618928" ID="ID_286121711" MODIFIED="1491816360920" TEXT="status: char(1), not null, default A">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      A: Active
    </p>
    <p>
      I: Inactive
    </p>
    <p>
      D: Deleted
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1477459863297" FOLDED="true" HGAP="49" ID="ID_1639454538" MODIFIED="1491816727259" POSITION="left" TEXT="acm_subject_teacher_map" VSHIFT="-3">
<icon BUILTIN="go"/>
<node CREATED="1475812249922" ID="ID_739478321" MODIFIED="1491816459708" TEXT="subject: int, fk(acm_subject: id), not null">
<arrowlink DESTINATION="ID_1485683775" ENDARROW="Default" ENDINCLINATION="259;0;" ID="Arrow_ID_755531469" STARTARROW="None" STARTINCLINATION="259;0;"/>
</node>
<node CREATED="1475813599682" ID="ID_1293063146" MODIFIED="1491816469923" TEXT="teacher: int, fk(sm_teacher: id), not null">
<arrowlink DESTINATION="ID_477875372" ENDARROW="Default" ENDINCLINATION="891;0;" ID="Arrow_ID_1741202118" STARTARROW="None" STARTINCLINATION="891;0;"/>
<arrowlink COLOR="#b0b0b0" DESTINATION="ID_1925000247" ENDARROW="Default" ENDINCLINATION="891;0;" ID="Arrow_ID_113345463" STARTARROW="None" STARTINCLINATION="891;0;"/>
</node>
</node>
<node CREATED="1475603071788" FOLDED="true" HGAP="47" ID="ID_140098921" MODIFIED="1491816934759" POSITION="left" TEXT="acm_standard_template">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      e.g. 5th, 6th, 7th, 8th
    </p>
  </body>
</html></richcontent>
<icon BUILTIN="go"/>
<node CREATED="1475205425343" ID="ID_1757961434" MODIFIED="1475836803137" TEXT="id: int, ai, pk">
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1757961434" ENDARROW="Default" ENDINCLINATION="401;0;" ID="Arrow_ID_1877609495" SOURCE="ID_796589400" STARTARROW="None" STARTINCLINATION="401;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1757961434" ENDARROW="Default" ENDINCLINATION="401;0;" ID="Arrow_ID_1200339825" SOURCE="ID_1172410115" STARTARROW="None" STARTINCLINATION="401;0;"/>
</node>
<node CREATED="1475602832679" ID="ID_1020818574" MODIFIED="1491816796340" TEXT="name: varchar(48), not null, unique"/>
<node CREATED="1491816754566" ID="ID_106056849" MODIFIED="1491816800652" TEXT="code: varchar(48), not null, unique"/>
<node CREATED="1476786632467" ID="ID_26677484" MODIFIED="1476786644576" TEXT="is_frozen: boolean , default False"/>
<node CREATED="1475205618928" ID="ID_174446557" MODIFIED="1476786644655" TEXT="status: char(1), not null, default A">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      A: Active
    </p>
    <p>
      I: Inactive
    </p>
    <p>
      D: Deleted
    </p>
    <p>
      F: Frozen
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1475811414453" FOLDED="true" HGAP="41" ID="ID_297650788" MODIFIED="1491816934760" POSITION="left" TEXT="acm_standard_template_subject_map" VSHIFT="2">
<icon BUILTIN="go"/>
<node CREATED="1475205425343" ID="ID_785380521" MODIFIED="1476722543464" TEXT="id: int, ai, pk"/>
<node CREATED="1475812222728" ID="ID_796589400" MODIFIED="1475837358099" TEXT="standard_template: int, fk(acm_standard_template: id), not null">
<arrowlink DESTINATION="ID_1757961434" ENDARROW="Default" ENDINCLINATION="401;0;" ID="Arrow_ID_1877609495" STARTARROW="None" STARTINCLINATION="401;0;"/>
</node>
<node CREATED="1475812249922" ID="ID_806215496" MODIFIED="1491816577386" TEXT="subject: int, fk(acm_subject: id), not null">
<arrowlink DESTINATION="ID_1485683775" ENDARROW="Default" ENDINCLINATION="399;0;" ID="Arrow_ID_341975188" STARTARROW="None" STARTINCLINATION="399;0;"/>
</node>
</node>
<node CREATED="1475836933192" FOLDED="true" HGAP="41" ID="ID_899039728" MODIFIED="1491822181319" POSITION="left" TEXT="acm_standard" VSHIFT="-3">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      e.g. - 8th (2015-16), 9th (2015-16), 10th (2015-16),8th (2014-15), 9th (2014-15), 10th (2014-15)
    </p>
  </body>
</html></richcontent>
<icon BUILTIN="go"/>
<node CREATED="1475205425343" ID="ID_1587492765" MODIFIED="1491822179515" TEXT="id: int, ai, pk">
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1587492765" ENDARROW="Default" ENDINCLINATION="286;0;" ID="Arrow_ID_24281923" SOURCE="ID_392910524" STARTARROW="None" STARTINCLINATION="286;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1587492765" ENDARROW="Default" ENDINCLINATION="336;0;" ID="Arrow_ID_223282008" SOURCE="ID_1660568458" STARTARROW="None" STARTINCLINATION="336;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1587492765" ENDARROW="Default" ENDINCLINATION="900;0;" ID="Arrow_ID_1268456209" SOURCE="ID_1444622867" STARTARROW="None" STARTINCLINATION="900;0;"/>
</node>
<node CREATED="1475602832679" ID="ID_1016002786" MODIFIED="1491816611270" TEXT="name: varchar(80), not null, unique"/>
<node CREATED="1475812222728" ID="ID_1172410115" MODIFIED="1475837363382" TEXT="standard_template: int, fk(acm_standard_template: id), not null">
<arrowlink DESTINATION="ID_1757961434" ENDARROW="Default" ENDINCLINATION="401;0;" ID="Arrow_ID_1200339825" STARTARROW="None" STARTINCLINATION="401;0;"/>
</node>
<node CREATED="1475837373533" ID="ID_311848433" MODIFIED="1491816622409" TEXT="academic_year: int, fk(acm_academic_year: id), not null">
<arrowlink DESTINATION="ID_1058266612" ENDARROW="Default" ENDINCLINATION="466;0;" ID="Arrow_ID_1888153003" STARTARROW="None" STARTINCLINATION="466;0;"/>
</node>
<node CREATED="1475205618928" ID="ID_1076976718" MODIFIED="1479894854002" TEXT="status: char(1), not null, default A">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      A: Active
    </p>
    <p>
      I: Inactive
    </p>
    <p>
      D: Deleted
    </p>
    <p>
      F: Frozen
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1475836933192" FOLDED="true" HGAP="40" ID="ID_461265827" MODIFIED="1491818991871" POSITION="left" TEXT="acm_standard_subject_map" VSHIFT="4">
<icon BUILTIN="go"/>
<node CREATED="1475205425343" ID="ID_1246281565" MODIFIED="1491818989634" TEXT="id: int, ai, pk">
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1246281565" ENDARROW="Default" ENDINCLINATION="318;0;" ID="Arrow_ID_1838815205" SOURCE="ID_10571724" STARTARROW="None" STARTINCLINATION="318;0;"/>
</node>
<node CREATED="1475837607062" ID="ID_392910524" MODIFIED="1475837627054" TEXT="standard: int, fk(acm_standard: id), not null">
<arrowlink DESTINATION="ID_1587492765" ENDARROW="Default" ENDINCLINATION="286;0;" ID="Arrow_ID_24281923" STARTARROW="None" STARTINCLINATION="286;0;"/>
</node>
<node CREATED="1475838797742" ID="ID_603658207" MODIFIED="1491816632529" TEXT="subject: int, fk(acm_subject: id), not null">
<arrowlink DESTINATION="ID_1485683775" ENDARROW="Default" ENDINCLINATION="497;0;" ID="Arrow_ID_892412924" STARTARROW="None" STARTINCLINATION="497;0;"/>
</node>
</node>
<node CREATED="1475206588678" FOLDED="true" HGAP="22" ID="ID_1407045081" MODIFIED="1491821027591" POSITION="right" TEXT="sm_teacher" VSHIFT="8">
<icon BUILTIN="go"/>
<node CREATED="1475205425343" ID="ID_477875372" MODIFIED="1491820453507" TEXT="id: int, ai, pk">
<linktarget COLOR="#b0b0b0" DESTINATION="ID_477875372" ENDARROW="Default" ENDINCLINATION="331;0;" ID="Arrow_ID_1526062388" SOURCE="ID_1691466592" STARTARROW="None" STARTINCLINATION="331;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_477875372" ENDARROW="Default" ENDINCLINATION="331;0;" ID="Arrow_ID_1269383389" SOURCE="ID_589790282" STARTARROW="None" STARTINCLINATION="331;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_477875372" ENDARROW="Default" ENDINCLINATION="891;0;" ID="Arrow_ID_1741202118" SOURCE="ID_1293063146" STARTARROW="None" STARTINCLINATION="891;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_477875372" ENDARROW="Default" ENDINCLINATION="943;0;" ID="Arrow_ID_1298025482" SOURCE="ID_1176691367" STARTARROW="None" STARTINCLINATION="943;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_477875372" ENDARROW="Default" ENDINCLINATION="315;0;" ID="Arrow_ID_909733133" SOURCE="ID_1483618441" STARTARROW="None" STARTINCLINATION="315;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_477875372" ENDARROW="Default" ENDINCLINATION="315;0;" ID="Arrow_ID_1680664043" SOURCE="ID_36444862" STARTARROW="None" STARTINCLINATION="315;0;"/>
</node>
<node CREATED="1491815985131" ID="ID_297229503" MODIFIED="1491816004507" TEXT="user: int, fk(user: id)">
<arrowlink DESTINATION="ID_506772145" ENDARROW="Default" ENDINCLINATION="651;0;" ID="Arrow_ID_376627978" STARTARROW="None" STARTINCLINATION="651;0;"/>
</node>
<node CREATED="1491816051838" ID="ID_960399255" MODIFIED="1491816067664" TEXT="employee_no: varchar(80), not null, unique"/>
</node>
<node CREATED="1491818175700" FOLDED="true" ID="ID_1443386810" MODIFIED="1491822934011" POSITION="right" TEXT="stm_student" VSHIFT="3">
<icon BUILTIN="go"/>
<node CREATED="1475205425343" ID="ID_1925000247" MODIFIED="1491822747018" TEXT="id: int, ai, pk">
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1925000247" ENDARROW="Default" ENDINCLINATION="331;0;" ID="Arrow_ID_214256554" SOURCE="ID_1691466592" STARTARROW="None" STARTINCLINATION="331;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1925000247" ENDARROW="Default" ENDINCLINATION="331;0;" ID="Arrow_ID_1114048425" SOURCE="ID_589790282" STARTARROW="None" STARTINCLINATION="331;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1925000247" ENDARROW="Default" ENDINCLINATION="891;0;" ID="Arrow_ID_113345463" SOURCE="ID_1293063146" STARTARROW="None" STARTINCLINATION="891;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1925000247" ENDARROW="Default" ENDINCLINATION="188;0;" ID="Arrow_ID_1988070654" SOURCE="ID_1082014886" STARTARROW="None" STARTINCLINATION="188;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1925000247" ENDARROW="Default" ENDINCLINATION="865;0;" ID="Arrow_ID_1397755240" SOURCE="ID_474782101" STARTARROW="None" STARTINCLINATION="865;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1925000247" ENDARROW="Default" ENDINCLINATION="865;0;" ID="Arrow_ID_1199479262" SOURCE="ID_1531889825" STARTARROW="None" STARTINCLINATION="865;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1925000247" ENDARROW="Default" ENDINCLINATION="946;0;" ID="Arrow_ID_1353125586" SOURCE="ID_658100040" STARTARROW="None" STARTINCLINATION="946;0;"/>
</node>
<node CREATED="1491815985131" ID="ID_10372465" MODIFIED="1491816004507" TEXT="user: int, fk(user: id)">
<arrowlink DESTINATION="ID_506772145" ENDARROW="Default" ENDINCLINATION="651;0;" ID="Arrow_ID_1501461064" STARTARROW="None" STARTINCLINATION="651;0;"/>
</node>
<node CREATED="1491816051838" ID="ID_1734577528" MODIFIED="1491818203662" TEXT="registration_no: varchar(80), not null, unique"/>
</node>
<node CREATED="1475812552102" FOLDED="true" HGAP="56" ID="ID_1446602425" MODIFIED="1491821019712" POSITION="left" TEXT="acm_division" VSHIFT="10">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      unique(name, standard)
    </p>
    <p>
      e.g. 9th(2015-16)-A, 9th(2015-16)-B, 9th(2015-16)-C
    </p>
  </body>
</html></richcontent>
<icon BUILTIN="go"/>
<node CREATED="1475205425343" ID="ID_1904693336" MODIFIED="1491821001080" TEXT="id: int, ai, pk">
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1904693336" ENDARROW="Default" ENDINCLINATION="222;0;" ID="Arrow_ID_1884456744" SOURCE="ID_1734435361" STARTARROW="None" STARTINCLINATION="222;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1904693336" ENDARROW="Default" ENDINCLINATION="851;0;" ID="Arrow_ID_744230897" SOURCE="ID_409398781" STARTARROW="None" STARTINCLINATION="851;0;"/>
</node>
<node CREATED="1475602832679" ID="ID_1341308252" MODIFIED="1491821007282" TEXT="name: varchar(12), not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      automatically determined -- standard-name + acadamic year name
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1475812222728" ID="ID_1660568458" MODIFIED="1477812399366" TEXT="standard: int, fk(acm_standard: id), not null">
<arrowlink DESTINATION="ID_1587492765" ENDARROW="Default" ENDINCLINATION="336;0;" ID="Arrow_ID_223282008" STARTARROW="None" STARTINCLINATION="336;0;"/>
</node>
<node CREATED="1475205618928" ID="ID_1242775822" MODIFIED="1491821007289" TEXT="status: char(1), not null, default A">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      A: Active
    </p>
    <p>
      I: Inactive
    </p>
    <p>
      D: Deleted
    </p>
    <p>
      F: Frozen
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1477479933198" FOLDED="true" HGAP="55" ID="ID_488137776" MODIFIED="1491822462051" POSITION="left" TEXT="acm_division_subject_map" VSHIFT="-7">
<icon BUILTIN="go"/>
<node CREATED="1477485846628" ID="ID_1478355089" MODIFIED="1491822416359" TEXT="id: int , ai, pk">
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1478355089" ENDARROW="Default" ENDINCLINATION="285;0;" ID="Arrow_ID_1446618747" SOURCE="ID_167979958" STARTARROW="None" STARTINCLINATION="285;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1478355089" ENDARROW="Default" ENDINCLINATION="1014;0;" ID="Arrow_ID_1465719904" SOURCE="ID_461826586" STARTARROW="None" STARTINCLINATION="1014;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1478355089" ENDARROW="Default" ENDINCLINATION="1014;0;" ID="Arrow_ID_1604632111" SOURCE="ID_1678141963" STARTARROW="None" STARTINCLINATION="1014;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1478355089" ENDARROW="Default" ENDINCLINATION="1077;0;" ID="Arrow_ID_519208654" SOURCE="ID_463299356" STARTARROW="None" STARTINCLINATION="1077;0;"/>
</node>
<node CREATED="1475838797742" ID="ID_855284857" MODIFIED="1475838826193" TEXT="subject: int, fk(acm_subject: id), not null">
<arrowlink DESTINATION="ID_1485683775" ENDARROW="Default" ENDINCLINATION="294;0;" ID="Arrow_ID_795597104" STARTARROW="None" STARTINCLINATION="294;0;"/>
</node>
<node CREATED="1477485897723" ID="ID_1734435361" MODIFIED="1491820175109" TEXT="division: int, fk(acm_division: id), not null">
<arrowlink DESTINATION="ID_1904693336" ENDARROW="Default" ENDINCLINATION="222;0;" ID="Arrow_ID_1884456744" STARTARROW="None" STARTINCLINATION="222;0;"/>
</node>
</node>
<node CREATED="1475813502445" FOLDED="true" HGAP="55" ID="ID_1613151247" MODIFIED="1491821007297" POSITION="left" TEXT="acm_division_subject_teacher_map" VSHIFT="-10">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      unique(batch_subject, teacher)
    </p>
  </body>
</html></richcontent>
<icon BUILTIN="go"/>
<node CREATED="1475813599682" ID="ID_1176691367" MODIFIED="1491818485196" TEXT="teacher: int, fk(am_teacher: id), not null">
<arrowlink DESTINATION="ID_477875372" ENDARROW="Default" ENDINCLINATION="943;0;" ID="Arrow_ID_1298025482" STARTARROW="None" STARTINCLINATION="943;0;"/>
</node>
<node CREATED="1477487071724" ID="ID_167979958" MODIFIED="1477487102970" TEXT="batch_subject: int, fk(bm_batch_subject: id), not null">
<arrowlink DESTINATION="ID_1478355089" ENDARROW="Default" ENDINCLINATION="285;0;" ID="Arrow_ID_1446618747" STARTARROW="None" STARTINCLINATION="285;0;"/>
</node>
</node>
<node CREATED="1475813101826" FOLDED="true" HGAP="70" ID="ID_1406548288" MODIFIED="1491819037685" POSITION="left" TEXT="sm_topic" VSHIFT="10">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      unique(standard_subject, name)
    </p>
    <p>
      
    </p>
    <p>
      e.g. Trignometry
    </p>
  </body>
</html></richcontent>
<icon BUILTIN="go"/>
<node CREATED="1475205425343" ID="ID_1579597924" MODIFIED="1475813396966" TEXT="id: int, ai, pk">
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1579597924" ENDARROW="Default" ENDINCLINATION="244;0;" ID="Arrow_ID_1584319490" SOURCE="ID_552062165" STARTARROW="None" STARTINCLINATION="244;0;"/>
</node>
<node CREATED="1475813186578" ID="ID_789465243" MODIFIED="1475813196484" TEXT="name: varchar(80), not null"/>
<node CREATED="1475813202078" ID="ID_10571724" MODIFIED="1491818989635" TEXT="standard_subject: int, fk(acm_standard_subject_map: id), not null">
<arrowlink DESTINATION="ID_1246281565" ENDARROW="Default" ENDINCLINATION="318;0;" ID="Arrow_ID_1838815205" STARTARROW="None" STARTINCLINATION="318;0;"/>
</node>
<node CREATED="1475813277741" ID="ID_270113444" MODIFIED="1475813306375" TEXT="duration: int, not null">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Duration required to teach this topic. in minutes
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1475205618928" ID="ID_1480144213" MODIFIED="1475813286571" TEXT="status: char(1), not null, default A">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      A: Active
    </p>
    <p>
      I: Inactive
    </p>
    <p>
      D: Deleted
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1475813322269" FOLDED="true" HGAP="78" ID="ID_1593718731" MODIFIED="1491819040405" POSITION="left" TEXT="sm_sub_topic" VSHIFT="-5">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      unique(sm_topic, name)
    </p>
    <p>
      
    </p>
    <p>
      e.g. Derivative , integration
    </p>
  </body>
</html></richcontent>
<icon BUILTIN="go"/>
<node CREATED="1475205425343" ID="ID_1221217368" MODIFIED="1479824317911" TEXT="id: int, ai, pk"/>
<node CREATED="1475813186578" ID="ID_1290501872" MODIFIED="1475813375893" TEXT="name: varchar(80), not null"/>
<node CREATED="1475813379369" ID="ID_552062165" MODIFIED="1491818943962" TEXT="sm_topic: int, fk(sm_topic: id), not null">
<arrowlink COLOR="#b0b0b0" DESTINATION="ID_1579597924" ENDARROW="Default" ENDINCLINATION="244;0;" ID="Arrow_ID_1584319490" STARTARROW="None" STARTINCLINATION="244;0;"/>
</node>
<node CREATED="1475205618928" ID="ID_1955380066" MODIFIED="1476722545058" TEXT="status: char(1), not null, default A">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      A: Active
    </p>
    <p>
      I: Inactive
    </p>
    <p>
      D: Deleted
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1491819238523" FOLDED="true" ID="ID_1982665912" MODIFIED="1491823272022" POSITION="right" TEXT="stm_student_division_map">
<icon BUILTIN="go"/>
<node CREATED="1491819315425" ID="ID_1082014886" MODIFIED="1491819329188" TEXT="student: int, fk(student: id)">
<arrowlink DESTINATION="ID_1925000247" ENDARROW="Default" ENDINCLINATION="188;0;" ID="Arrow_ID_1988070654" STARTARROW="None" STARTINCLINATION="188;0;"/>
</node>
<node CREATED="1491819335105" ID="ID_409398781" MODIFIED="1491819357437" TEXT="division: int, fk(division: id)">
<arrowlink DESTINATION="ID_1904693336" ENDARROW="Default" ENDINCLINATION="851;0;" ID="Arrow_ID_744230897" STARTARROW="None" STARTINCLINATION="851;0;"/>
</node>
<node CREATED="1491819402120" ID="ID_1691316906" MODIFIED="1491819428770" TEXT="admission_date: datetime, not null"/>
<node CREATED="1491819472463" ID="ID_744758365" MODIFIED="1491819484017" TEXT="passout_date: datetime, null"/>
<node CREATED="1491819494270" ID="ID_498560240" MODIFIED="1491819509967" TEXT="previous_division_id: int, null"/>
</node>
<node CREATED="1475933980367" FOLDED="true" ID="ID_341908173" MODIFIED="1491821057883" POSITION="right" TEXT="tp_lecture">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      unique(name, division_subject)
    </p>
    <p>
      
    </p>
    <p>
      Need to review
    </p>
  </body>
</html></richcontent>
<icon BUILTIN="go"/>
<node CREATED="1475915510894" ID="ID_271798092" MODIFIED="1475934847486" TEXT="id: int, ai, pk"/>
<node CREATED="1475933794475" ID="ID_1326259082" MODIFIED="1475933806347" TEXT="name: varchar(48), not null"/>
<node CREATED="1475934018421" ID="ID_924360525" MODIFIED="1475934026612" TEXT="from_date: datetime, not null"/>
<node CREATED="1475934029871" ID="ID_254234360" MODIFIED="1475934037200" TEXT="to_date: datetime, not null"/>
<node CREATED="1475934121541" ID="ID_461826586" MODIFIED="1491821006675" TEXT="division_subject: int, fk(acm_division_subject: id), not null">
<arrowlink DESTINATION="ID_1478355089" ENDARROW="Default" ENDINCLINATION="1014;0;" ID="Arrow_ID_1465719904" STARTARROW="None" STARTINCLINATION="1014;0;"/>
</node>
<node CREATED="1491820429703" ID="ID_1483618441" MODIFIED="1491820453507" TEXT="teacher: int, fk(sm_teacher: id), not null">
<arrowlink DESTINATION="ID_477875372" ENDARROW="Default" ENDINCLINATION="315;0;" ID="Arrow_ID_909733133" STARTARROW="None" STARTINCLINATION="315;0;"/>
</node>
<node CREATED="1475205618928" ID="ID_558831053" MODIFIED="1491820230904" TEXT="status: char(1), not null, default A">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      A: Active
    </p>
    <p>
      I: Inactive
    </p>
    <p>
      D: Deleted
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1491820038142" FOLDED="true" ID="ID_196966452" MODIFIED="1491820403456" POSITION="right" TEXT="tp_resource_type">
<icon BUILTIN="go"/>
<node CREATED="1475915510894" ID="ID_1713056640" MODIFIED="1491822041729" TEXT="id: int, ai, pk">
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1713056640" ENDARROW="Default" ENDINCLINATION="193;0;" ID="Arrow_ID_1057300378" SOURCE="ID_913479558" STARTARROW="None" STARTINCLINATION="193;0;"/>
</node>
<node CREATED="1475933794475" ID="ID_1411178392" MODIFIED="1491820065550" TEXT="name: varchar(48), not null, unique"/>
<node CREATED="1475205618928" ID="ID_1290202415" MODIFIED="1475934151205" TEXT="status: char(1), not null, default A">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      A: Active
    </p>
    <p>
      I: Inactive
    </p>
    <p>
      D: Deleted
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1491820038142" FOLDED="true" ID="ID_1116040218" MODIFIED="1491821950394" POSITION="right" TEXT="tp_resource">
<icon BUILTIN="go"/>
<node CREATED="1475915510894" ID="ID_329941298" MODIFIED="1491820379116" TEXT="id: int, ai, pk">
<linktarget COLOR="#b0b0b0" DESTINATION="ID_329941298" ENDARROW="Default" ENDINCLINATION="285;0;" ID="Arrow_ID_1597999425" SOURCE="ID_715658062" STARTARROW="None" STARTINCLINATION="285;0;"/>
</node>
<node CREATED="1475933794475" ID="ID_624600442" MODIFIED="1491820094447" TEXT="name: varchar(48), not null"/>
<node CREATED="1491820097581" ID="ID_913479558" MODIFIED="1491820120977" TEXT="resource_type: int, fk(tp_resource_type: id)">
<arrowlink DESTINATION="ID_1713056640" ENDARROW="Default" ENDINCLINATION="193;0;" ID="Arrow_ID_1057300378" STARTARROW="None" STARTINCLINATION="193;0;"/>
</node>
<node CREATED="1475205618928" ID="ID_1555859521" MODIFIED="1491820117696" TEXT="status: char(1), not null, default A">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      A: Active
    </p>
    <p>
      I: Inactive
    </p>
    <p>
      D: Deleted
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1491820318321" FOLDED="true" ID="ID_570740687" MODIFIED="1491820383376" POSITION="right" TEXT="tp_lecture_resource_map">
<icon BUILTIN="go"/>
<node CREATED="1491820337185" ID="ID_1594793882" MODIFIED="1491820352788" TEXT="lecture: int, fk(tp_lecture: id), not null"/>
<node CREATED="1491820357992" ID="ID_715658062" MODIFIED="1491820379117" TEXT="resource: int, fk(tp_resource: id), not null">
<arrowlink DESTINATION="ID_329941298" ENDARROW="Default" ENDINCLINATION="285;0;" ID="Arrow_ID_1597999425" STARTARROW="None" STARTINCLINATION="285;0;"/>
<arrowlink COLOR="#b0b0b0" DESTINATION="ID_782065745" ENDARROW="Default" ENDINCLINATION="285;0;" ID="Arrow_ID_79347252" STARTARROW="None" STARTINCLINATION="285;0;"/>
</node>
</node>
<node CREATED="1475934393563" FOLDED="true" HGAP="75" ID="ID_1591729288" MODIFIED="1491821713022" POSITION="left" TEXT="atm_attendance" VSHIFT="-18">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      unique(student, date)
    </p>
  </body>
</html></richcontent>
<icon BUILTIN="go"/>
<node CREATED="1475915510894" ID="ID_1879831804" MODIFIED="1475933822794" TEXT="id: int, ai, pk"/>
<node CREATED="1475934433283" ID="ID_606242184" MODIFIED="1475934448635" TEXT="in_time: datetime, not null"/>
<node CREATED="1475934433283" ID="ID_1017926681" MODIFIED="1491820622279" TEXT="out_time: datetime, not null"/>
<node CREATED="1491821331155" ID="ID_1134268534" MODIFIED="1491821338664" TEXT="date: datetime. not null"/>
<node CREATED="1475934935734" ID="ID_474782101" MODIFIED="1491820655281" TEXT="student: int, fk(stm_student: id), not null">
<arrowlink DESTINATION="ID_1925000247" ENDARROW="Default" ENDINCLINATION="865;0;" ID="Arrow_ID_1397755240" STARTARROW="None" STARTINCLINATION="865;0;"/>
</node>
</node>
<node CREATED="1475933980367" FOLDED="true" HGAP="106" ID="ID_1967861894" MODIFIED="1491823292545" POSITION="left" TEXT="hm_homework" VSHIFT="-15">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      unique(name, batch_subject)
    </p>
    <p>
      
    </p>
    <p>
      Need to review
    </p>
  </body>
</html></richcontent>
<icon BUILTIN="go"/>
<node CREATED="1475915510894" ID="ID_1408909759" MODIFIED="1491821199666" TEXT="id: int, ai, pk">
<linktarget COLOR="#b0b0b0" DESTINATION="ID_1408909759" ENDARROW="Default" ENDINCLINATION="331;0;" ID="Arrow_ID_1811049046" SOURCE="ID_729580629" STARTARROW="None" STARTINCLINATION="331;0;"/>
</node>
<node CREATED="1475933794475" ID="ID_317630694" MODIFIED="1491821120992" TEXT="text: TextField, not null"/>
<node CREATED="1475934018421" ID="ID_588370044" MODIFIED="1491821109168" TEXT="given_date: datetime, not null"/>
<node CREATED="1475934029871" ID="ID_1158043142" MODIFIED="1491821130333" TEXT="submission_date: datetime, not null"/>
<node CREATED="1475934121541" ID="ID_1678141963" MODIFIED="1491821006675" TEXT="division_subject: int, fk(acm_division_subject: id), not null">
<arrowlink DESTINATION="ID_1478355089" ENDARROW="Default" ENDINCLINATION="1014;0;" ID="Arrow_ID_1604632111" STARTARROW="None" STARTINCLINATION="1014;0;"/>
</node>
<node CREATED="1491820429703" ID="ID_36444862" MODIFIED="1491820453507" TEXT="teacher: int, fk(sm_teacher: id), not null">
<arrowlink DESTINATION="ID_477875372" ENDARROW="Default" ENDINCLINATION="315;0;" ID="Arrow_ID_1680664043" STARTARROW="None" STARTINCLINATION="315;0;"/>
</node>
<node CREATED="1475205618928" ID="ID_1119666520" MODIFIED="1491820230904" TEXT="status: char(1), not null, default A">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      A: Active
    </p>
    <p>
      I: Inactive
    </p>
    <p>
      D: Deleted
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1491821142718" FOLDED="true" HGAP="118" ID="ID_9147965" MODIFIED="1491821970642" POSITION="left" TEXT="hm_homework_student_map" VSHIFT="-21">
<icon BUILTIN="go"/>
<node CREATED="1475915510894" ID="ID_1790657551" MODIFIED="1491821162582" TEXT="id: int, ai, pk"/>
<node CREATED="1491821172437" ID="ID_729580629" MODIFIED="1491821543962" TEXT="home_work: int, fk(hm_homework: id), not null">
<arrowlink DESTINATION="ID_1408909759" ENDARROW="Default" ENDINCLINATION="331;0;" ID="Arrow_ID_1811049046" STARTARROW="None" STARTINCLINATION="331;0;"/>
</node>
<node CREATED="1475934935734" ID="ID_1531889825" MODIFIED="1491820655281" TEXT="student: int, fk(stm_student: id), not null">
<arrowlink DESTINATION="ID_1925000247" ENDARROW="Default" ENDINCLINATION="865;0;" ID="Arrow_ID_1199479262" STARTARROW="None" STARTINCLINATION="865;0;"/>
</node>
</node>
<node CREATED="1491821870683" FOLDED="true" ID="ID_177156949" MODIFIED="1491822164911" POSITION="right" TEXT="em_exam_type" VSHIFT="38">
<icon BUILTIN="go"/>
<node CREATED="1475915510894" ID="ID_600982092" MODIFIED="1491822044292" TEXT="id: int, ai, pk">
<linktarget COLOR="#b0b0b0" DESTINATION="ID_600982092" ENDARROW="Default" ENDINCLINATION="161;0;" ID="Arrow_ID_1640594030" SOURCE="ID_799558688" STARTARROW="None" STARTINCLINATION="161;0;"/>
</node>
<node CREATED="1491821930818" ID="ID_1831542667" MODIFIED="1491821942397" TEXT="name: varchar(48), not null, unique"/>
<node CREATED="1475205618928" ID="ID_405450251" MODIFIED="1491820117696" TEXT="status: char(1), not null, default A">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      A: Active
    </p>
    <p>
      I: Inactive
    </p>
    <p>
      D: Deleted
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1491820038142" FOLDED="true" ID="ID_1720825540" MODIFIED="1491822934011" POSITION="right" TEXT="em_exam">
<icon BUILTIN="go"/>
<node CREATED="1475915510894" ID="ID_782065745" MODIFIED="1491822369568" TEXT="id: int, ai, pk">
<linktarget COLOR="#b0b0b0" DESTINATION="ID_782065745" ENDARROW="Default" ENDINCLINATION="285;0;" ID="Arrow_ID_79347252" SOURCE="ID_715658062" STARTARROW="None" STARTINCLINATION="285;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_782065745" ENDARROW="Default" ENDINCLINATION="252;0;" ID="Arrow_ID_1417765863" SOURCE="ID_1029602054" STARTARROW="None" STARTINCLINATION="252;0;"/>
</node>
<node CREATED="1475933794475" ID="ID_565708926" MODIFIED="1491820094447" TEXT="name: varchar(48), not null"/>
<node CREATED="1491820097581" ID="ID_799558688" MODIFIED="1491822044293" TEXT="exam_type: int, fk(em_exam_type: id)">
<arrowlink DESTINATION="ID_600982092" ENDARROW="Default" ENDINCLINATION="161;0;" ID="Arrow_ID_1640594030" STARTARROW="None" STARTINCLINATION="161;0;"/>
</node>
<node CREATED="1491822078224" ID="ID_1134237541" MODIFIED="1491822086935" TEXT="from_date: datetime , not null"/>
<node CREATED="1491822078224" ID="ID_57498219" MODIFIED="1491822095042" TEXT="to_date: datetime , not null"/>
<node CREATED="1491822143057" ID="ID_1444622867" MODIFIED="1491822179515" TEXT="standard: int, fk(standard: id), not null">
<arrowlink DESTINATION="ID_1587492765" ENDARROW="Default" ENDINCLINATION="900;0;" ID="Arrow_ID_1268456209" STARTARROW="None" STARTINCLINATION="900;0;"/>
</node>
<node CREATED="1491822540793" ID="ID_1423906325" MODIFIED="1491822854079" TEXT="time_table_published: boolean, default False"/>
<node CREATED="1491822540793" ID="ID_511343448" MODIFIED="1491822868958" TEXT="result_published: boolean, default False"/>
<node CREATED="1475205618928" ID="ID_1630568187" MODIFIED="1491822086940" TEXT="status: char(1), not null, default A">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      A: Active
    </p>
    <p>
      I: Inactive
    </p>
    <p>
      D: Deleted
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1491822334308" FOLDED="true" HGAP="23" ID="ID_682772354" MODIFIED="1491822948786" POSITION="right" TEXT="em_exam_subject_map" VSHIFT="-23">
<icon BUILTIN="go"/>
<node CREATED="1491822690343" ID="ID_193999303" MODIFIED="1491822702899" TEXT="id: int, not null, ai pk">
<linktarget COLOR="#b0b0b0" DESTINATION="ID_193999303" ENDARROW="Default" ENDINCLINATION="1065;0;" ID="Arrow_ID_1983128672" SOURCE="ID_955724445" STARTARROW="None" STARTINCLINATION="1065;0;"/>
</node>
<node CREATED="1491822350508" ID="ID_1029602054" MODIFIED="1491822369568" TEXT="exam: int, fk(em_exam: id), not null">
<arrowlink DESTINATION="ID_782065745" ENDARROW="Default" ENDINCLINATION="252;0;" ID="Arrow_ID_1417765863" STARTARROW="None" STARTINCLINATION="252;0;"/>
</node>
<node CREATED="1491822376284" ID="ID_463299356" MODIFIED="1491822416359" TEXT="division_subject: int, fk(division_subject: id), not null">
<arrowlink DESTINATION="ID_1478355089" ENDARROW="Default" ENDINCLINATION="1077;0;" ID="Arrow_ID_519208654" STARTARROW="None" STARTINCLINATION="1077;0;"/>
</node>
<node CREATED="1491822078224" ID="ID_424517503" MODIFIED="1491822086935" TEXT="from_date: datetime , not null"/>
<node CREATED="1491822078224" ID="ID_716775812" MODIFIED="1491822095042" TEXT="to_date: datetime , not null"/>
<node CREATED="1491822780950" ID="ID_906661463" MODIFIED="1491822792140" TEXT="total_marks: int, not null"/>
<node CREATED="1475205618928" ID="ID_410845513" MODIFIED="1491822698313" TEXT="status: char(1), not null, default A">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      A: Active
    </p>
    <p>
      I: Inactive
    </p>
    <p>
      D: Deleted
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1491822628976" FOLDED="true" HGAP="109" ID="ID_1898906524" MODIFIED="1491822951506" POSITION="left" TEXT="rm_appearance" VSHIFT="-2">
<icon BUILTIN="go"/>
<node CREATED="1491822653423" ID="ID_955724445" MODIFIED="1491822702899" TEXT="exam_subject: int, fk(em_exam_subject_map: id)">
<arrowlink DESTINATION="ID_193999303" ENDARROW="Default" ENDINCLINATION="1065;0;" ID="Arrow_ID_1983128672" STARTARROW="None" STARTINCLINATION="1065;0;"/>
</node>
<node CREATED="1491822712607" ID="ID_658100040" MODIFIED="1491822747018" TEXT="student: int, fk(stm_student: id), not null">
<arrowlink DESTINATION="ID_1925000247" ENDARROW="Default" ENDINCLINATION="946;0;" ID="Arrow_ID_1353125586" STARTARROW="None" STARTINCLINATION="946;0;"/>
</node>
<node CREATED="1491822751350" ID="ID_755327334" MODIFIED="1491822757824" TEXT="started_at: datetime, null"/>
<node CREATED="1491822751350" ID="ID_766465512" MODIFIED="1491822766792" TEXT="ended_at: datetime, null"/>
<node CREATED="1491822795373" ID="ID_1628244267" MODIFIED="1491822806082" TEXT="obtained_marks: int, null"/>
</node>
</node>
</map>
