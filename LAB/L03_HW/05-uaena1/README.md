<div id="current" aria-labelledby="ui-id-17" role="tabpanel" class="ui-tabs-panel ui-corner-bottom ui-widget-content" aria-hidden="false">
    <form method="post" action="/elab/lab/submit/1023/11594/19056/" enctype="multipart/form-data" autocomplete="off">
      <div id="assignment-body">
        <input type="hidden" name="csrfmiddlewaretoken" value="4K2UfRdQii4SRWO0iGiwfGHCZt0tmDv8tmq1GOr9yVwHZAzr8ODzj2wC1b1z4ILI">
        <h1>UAENA 1 : ยูแอนา 1</h1><p>เมื่อวันที่ 16 พฤษภาคมที่ผ่านมา เป็นวันครบรอบวันเกิดของ <strong>IU</strong> นักร้องสาวสุดน่ารักขวัญใจใครหลายๆ คนในที่นี้ </p><p>โดยในเที่ยงคืนของวันนั้น (เวลาเกาหลี) พี่ลี่ของเราได้โพสรูปตัวเองใส่ชุดสีแดง ทำให้ชาวยูแอนา (เหล่าแฟนคลับของไอยู) ได้หายคิดถึงกันบ้าง</p><p>แต่อย่างที่เหล่ายูแอนาทราบกันดีว่า ตอนนี้พี่ลี่กำลังถ่ายหนังเรื่องใหม่ <strong>Dream</strong> โดยพี่ลี่รับบทเป็น อีโซมิน โปรดิวเซอร์สาวที่มีความฝันในการที่จะประสบความสำเร็จในหน้าที่การงาน </p><p>อีกทั้งสถานการณ์การแพร่ระบาดของโรคโควิด 19 ทำให้ตั้งแต่วันนั้น พี่ลี่ของเราไม่ได้โพสรูปตัวเองลงไอจีอีกเลย. ซึ่งทำให้เหล่ายูแอนาต่างคิดถึงแทบใจจะขาด </p><p>นายเอ ซึ่งเป็นยูแอนาตัวยง </p><p>ก็ได้ซื้อ <strong>Photobook</strong> และ <strong>Album</strong> ของไอยูเป็นจำนวนมาก เพื่อเป็นการสนับสนุนพี่ลี่ทางตรง</p><p>ซึ่งในช่วงเวลาที่พี่ลี่ไม่ได้โพสรูป นายเอก็ได้เอา Photobook กับ Album มาดูเป็นของต่างหน้า แล้วนายเอก็ฉุกคิดได้ว่า</p><p><strong>'ของที่เราซื้อมามันเป็นของแท้หรือป่าวนะ ?'</strong></p><p>โดยเราสามารถตรวจสอบว่าเป็นของแท้หรือของปลอมได้ โดยการนำรหัสสินค้าซึ่งเป็น<strong>ตัวอักษรภาษาอังกฤษ</strong> ไปตรวจสอบ</p><p>ถ้าเป็น <strong>Photobook</strong> รหัสสินค้าจะเป็นตัวพิมพ์ใหญ่</p><p>ถ้าเป็น <strong>Album</strong> รหัสสินค้าจะเป็นตัวพิมพ์เล็ก</p><p>และถ้าเป็นของแท้ <strong>ตัวอักษรตัวสุดท้ายจะมีค่าเท่ากับ ตัวอักษรที่อยู่ถัดไปจากตัวแรก</strong></p><p>เช่น <strong>e</strong>heartoo<strong>f</strong> รหัสสินค้านี้เป็น Album เพราะเป็นตัวพิมพ์เล็ก และเป็นของแท้เพราะ f ซึ่งเป็นตัวอักษรตัวสุดท้ายอยู่ถัดจาก e ซึ่งเป็นตัวอักษรตัวแรก</p><h1>นิยามฟังก์ชั่นที่ต้องสร้าง</h1><style>
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
</style>
<table>
    <tbody><tr>
        <th>
            ชื่อฟังก์ชันและรูปแบบของพารามิเตอร์
        </th>
        <th>
            คำอธิบายของฟังก์ชัน
        </th>
        <th>
            รูปแบบการคืนค่า
        </th>
    </tr>
    <tr>
        <td>
            What(str)
        </td>
        <td>
           เป็นฟังก์ชันที่ใช้ตรวจสอบว่ารหัสสินค้าเป็น Photobook หรือ Album 
        </td>
        <td>
           <b>"Photobook"</b> เมื่อพารามิเตอร์ที่รับเข้ามา เป็นรหัสสินค้าของ Photobook<br>
           <b>"Album"</b> เมื่อพารามิเตอร์ที่รับเข้ามา เป็นรหัสสินค้าของ Album<br>
        </td>

    </tr>
    <tr>
        <td>
            SStatus()
        </td>
        <td>
           เป็นฟังก์ชันที่ใช้แสดงว่ารหัสสินค้าเป็น Photobook หรือ Album (ฟังก์ชันนี้ไม่ได้ใส่ค่าใดๆลงไป ดังนั้นผู้เขียนควรดึงค่าตัวแปรจากภายนอกฟังก์ชันมาทำให้ฟังก์ชันสมบูรณ์) (รับประกันว่าจะใช้งานก็ต่อเมื่อใช้งาน What(str) ไปแล้ว)
        </td>
        <td>
           <b>"Photobook"</b> เมื่อรหัสสินค้าที่เคยทดสอบไปเป็น Photobook<br>
           <b>"Album"</b> เมื่อรหัสสินค้าที่เคยทดสอบไปเป็น Album<br>
        </td>

    </tr>
    <tr>
        <td>
            RReal(str)
        </td>
        <td>
            ฟังก์ชันที่ไว้เช็คว่าเป็นของแท้ไหม
        </td>
        <td>
           <b>True</b> เมื่อเป็นของแท้
           <b>False</b> เมื่อไม่เป็นของแท้
        </td>
    </tr>
</tbody></table>
<p><strong>ขออภัยที่เขียนโจทย์ไม่ละเอียด ภายในฟังก์ชัน ไม่ต้องมีการ print ค่าใดๆออกมา</strong></p><h1>ข้อมูลนำเข้า</h1><p> ตัวอักษรแสดงรหัสสินค้า ความยาวไม่เกิน 15 ตัวอักษร เป็นพิมพ์ใหญ่ไม่ก็พิมพ์เล็กล้วน และไม่มีตัวอักษร z, Z อยู่ในรหัส</p><h1>ข้อมูลส่งออก</h1><p> <strong>บรรทัดที่ 1 :</strong> บอกชนิดของสินค้าว่าเป็น Photobook หรือ Album</p><p> <strong>บรรทัดที่ 2 :</strong> บอกว่าสินค้านี้เป็นของแท้หรือไม่</p><h1>ตัวอย่างที่ 1</h1><p></p><pre class="output"><em>eheartoof</em>
Album
True
</pre><p></p><h1>ตัวอย่างที่ 2</h1><p></p><pre class="output"><em>ISASO</em>
Photobook
False
</pre><p></p><h1>เมื่อรันใน Python shell ควรได้ผลลัพธ์ดังนี้ (เมื่อตั้งชื่อโปรแกรมว่า uaena1.py)</h1><p><strong>คนที่รันใน repl.it ให้เปลี่ยนจาก uaena เป็น main</strong>
</p><pre class="output"><span class="console">&gt;</span>$ <em>python</em>
<span class="console">&gt;&gt;&gt; </span><em>import uaena1</em>
<span class="console">&gt;&gt;&gt; </span><em>x = 'ISASO'</em>
<span class="console">&gt;&gt;&gt; </span><em>uaena1.SStatus()</em>
Dont Check
<span class="console">&gt;&gt;&gt; </span><em>uaena1.What(x)</em>
Photobook
<span class="console">&gt;&gt;&gt; </span><em>uaena1.SStatus()</em>
Photobook
<span class="console">&gt;&gt;&gt; </span><em>uaena1.RReal(x)</em>
False<p></p></pre>
<p></p><fieldset><pre><div class="code-menu"><a href="#" class="lineno-toggle">[hide line #]</a></div><code class="source"><textarea class="codeblank" cols="44" name="b1" rows="30" wrap="off" autocomplete="off"></textarea></code></pre></fieldset><p></p><p></p><p>และน้องๆ ได้ความรู้อะไรบ้างจากการทำโจทย์ข้อนี้</p><p>{{</p> 
      </div>
      
      
    </form>
  </div>