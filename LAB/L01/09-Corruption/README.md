<div id="current" aria-labelledby="ui-id-33" role="tabpanel" class="ui-tabs-panel ui-corner-bottom ui-widget-content" aria-hidden="false">
    <form method="post" action="/elab/lab/submit/1023/11527/18991/" enctype="multipart/form-data" autocomplete="off">
      <div id="assignment-body">
        <input type="hidden" name="csrfmiddlewaretoken" value="DXJ7FkBBSmLr12EdOno0p2GHlsEAvR3g2z7e6hPU8Zdg9GpEEvJ3tovHnaFGdWjQ">
        <h1>เสาไฟกินรี 1 - corruption</h1><p>จากข่าวเสาไฟกินรีอันโด่งดังของอบต.ราชเทวะ จะเห็นได้ว่าในอนาคตอาจจะเกิดกรณีการสร้างเสาไฟฟ้าในรูปแบบนี้ได้เพิ่มอีกเป็นจำนวนมาก </p><p>และแน่นอนว่าจะต้องทำให้เกิดข้อสงสัยแบบนี้อีกแน่นอน ดังนั้นเหล่ารุ่นพี่มหาวิทยาลัยเกษตรศาสตร์ภาควิชาวิศวกรรมคอมพิวเตอร์จึงต้องการช่วยเหลือทั้งภาครัฐและประชาชน </p><p>โดยทำการหาข้อมูลความสูงของเสาไฟประกอบกับงบประมาณที่ใช้ในการสร้างเสาไฟขึ้นมา เพื่อเอาไว้ทดสอบว่า การสร้างเสาไฟในรูปแบบต่างๆแบบไหนที่สามารถเป็นการสร้างแบบทุจริตได้บ้าง </p><p>โดยมีข้อมูลดังตารางนี้
<style>
table {
  border-collapse: collapse;
  width: 50%;
}
td, th {
  border: 2px solid #000000;
  text-align: left;
  padding: 6px;
}
th {
  background-color: #dddddd;
}
</style></p><table>
  <tbody><tr>
    <th>ความสูงของเสาไฟฟ้า </th>
    <th>ราคาของเสาไฟฟ้าต่อต้น </th>
  </tr>
  <tr>
    <td>ไม่เกิน 1 เมตร</td>
    <td>ไม่เกิน 1000 บาท</td>
  </tr>
  <tr>
    <td>มากกว่า 1 เมตร แต่ไม่เกิน 4 เมตร</td>
    <td>ไม่เกิน 5000 บาท</td>
  </tr>
  <tr>
    <td>มากกว่า 4 เมตร แต่ไม่เกิน 8 เมตร</td>
    <td>ไม่เกิน 30000 บาท</td>
  </tr>
  <tr>
    <td>มากกว่า 8 เมตร</td>
    <td>ไม่เกิน 75000 บาท</td>
  </tr>
</tbody></table>
<p><em>ข้อมูลที่ให้มานี้ไม่ได้เกี่ยวข้องกับความเป็นจริงแต่ประการใด</em></p><p>และนำข้อมูลในตารางมาเขียนโปรแกรม เพื่อทดสอบการทุจริตของโครงการสร้างเสาไฟ แต่รุ่นพี่ตอนนี้ไม่มีใครว่างเลยจึงต้องขอความช่วยเหลือจากรุ่นน้องในการเขียนโปรแกรมนี้ โดยจะมี </p><p><strong>ข้อมูลนำเข้า</strong></p><p>บรรทัดที่ 1 : ความสูงของเสาไฟฟ้า (เมตร) เป็นจำนวนเต็มหรือเลขทศนิยม</p><p>บรรทัดที่ 2 : ราคาของเสาไฟฟ้า (บาท)</p><p><strong>ข้อมูลส่งออก</strong></p><p>บรรทัดที่ 1 : ผลว่าทุจริตหรือไม่ ( YES : มีการทุจริต, NO : ไม่มีการทุจริต )</p><h2>Example1</h2><p></p><pre class="output">Hight : <em>0.52</em>
Cost : <em>112</em>
NO
</pre><p></p><h2>Example2</h2><p></p><pre class="output">Hight : <em>3</em>
Cost : <em>5600.05</em>
YES
</pre><p></p><h2>Example3</h2><p></p><pre class="output">Hight : <em>10</em>
Cost : <em>94884</em>
YES