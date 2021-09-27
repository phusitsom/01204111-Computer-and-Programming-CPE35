<div id="current" aria-labelledby="ui-id-13" role="tabpanel" class="ui-tabs-panel ui-corner-bottom ui-widget-content" aria-hidden="false">
    <form method="post" action="/elab/lab/submit/1023/11635/19095/" enctype="multipart/form-data" autocomplete="off">
      <div id="assignment-body">
        <input type="hidden" name="csrfmiddlewaretoken" value="X5wgc8Uf4C5ieglQYl37uNl68ObzBKBjmHUnD58ykfx7mU6hOtoay9a6awcFjPRT">
        <h1><strong>Add &amp; Remove</strong></h1><p>ในสัปดาห์นี้ น้องๆ ได้คงเรียนการใช้ list พื้นฐานกันบ้างแล้ว โจทย์ข้อนี้จะเป็นการฝึกให้น้องใช้การดำเนินการต่างของ list 
ให้ชำนาญมากยิ่งขึ้น</p><p>จงรับค่าจำนวนเต็ม แล้วนำตัวเลขเหล่านั้นเก็บเข้าใน list และรับคำสั่งในการเปลี่ยนแปลง list จนกว่าผู้ใช้จะป้อนคำสั่งให้หยุด เมื่อจบคำสั่งแล้ว ให้แสดงหน้าตาของ list ล่าสุดด้วย</p><p>โดยโปรแกรมจะมีการดำเนินการต่างๆ ดังนี้</p><style>
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
            รูปแบบคำสั่ง
        </th>
        <th>
            คำอธิบายของคำสั่ง
        </th>

    </tr>
    <tr>
        <td>
            <b>A x</b>
        </td>
        <td>
           เพิ่มจำนวนเต็ม x ต่อท้ายลงใน list 
        </td>


    </tr>
    <tr>
        <td>
            <b>S x</b>
        </td>
        <td>
            แสดงข้อมูลของ list ในช่องที่ x (ช่องเริ่มต้นที่ 0 และรับประกันชุดข้อมูลทดสอบว่าจะไม่เรียกแสดงช่องข้อมูลที่เกินขนาดของ list)
        </td>


    </tr>
    <tr>
        <td>
            <b>R x</b>
        </td>
        <td>
            ลบข้อมูลใน list ช่องที่ x 
        </td>
    </tr>
    <tr>
        <td>
            <b>E 0</b>
        </td>
        <td>
            คำสั่งบอกการยกเลิกรับคำสั่งของผู้ใช้ 
        </td>
    </tr>
</tbody></table>
<p><strong>คำแนะนำในการรับค่า</strong></p><pre class="output">ส่วนการรับค่าตัวเลขลงใน list 
A = list(map(int,input().split()))

===================

ส่วนการรับค่าคำสั่ง
menu,x = input().split()
x = int(x)

ในที่นี้เราจะได้ menu เป็นตัวแปรประเภท string และ x เป็น integer
</pre>
<h2>Example 1</h2><p></p><pre class="output"><em>1 2 3 4 5</em>
<em>A 100</em>
<em>A 200</em>
<em>S 6</em>
200
<em>R 5</em>
<em>E 0</em>
1 2 3 4 5 200
</pre><p></p><h2>Example 2</h2><p></p><pre class="output"><em>1 2 3 4 5</em>
<em>R 0</em>
<em>R 0</em>
<em>R 0</em>
<em>R 0</em>
<em>R 0</em>
<em>E 0</em><p></p></pre>
<p></p><fieldset><pre><div class="code-menu"><a href="#" class="lineno-toggle">[hide line #]</a></div><code class="source"><textarea class="codeblank" cols="40" name="b1" rows="14" wrap="off" autocomplete="off"></textarea></code></pre></fieldset><p></p><p>และน้องๆ ได้ความรู้อะไรบ้างจากการทำโจทย์ข้อนี้</p><p><input class="textblank" name="b2" size="76" type="text" value=""></p> 
      </div>
      
      
    </form>
  </div>