<div id="current" aria-labelledby="ui-id-1" role="tabpanel" class="ui-tabs-panel ui-corner-bottom ui-widget-content" aria-hidden="false">
    <form method="post" action="/elab/lab/submit/1023/11594/19049/" enctype="multipart/form-data" autocomplete="off">
      <div id="assignment-body">
        <input type="hidden" name="csrfmiddlewaretoken" value="5wGKTJg5VWWqPYF3M3ApatTMDa20LLYqu84RkGuobzofXCquCbVsePIMFS36tQe0">
        <h1>[Contractor] ผู้รับเหมาก่อสร้าง</h1><p>ผู้รับเหมาก่อสร้างได้รับงานสร้างรูปปั้นเชิดชูเกียรติ จึงได้ติดต่อจ้างน้องๆ CPE 35 ให้ทำโปรแกรมรับคำสั่งจากลูกค้าว่าจะสร้างเป็นรูปทรงอะไร ขนาดเท่าไหร่ จากนั้นทำการคำนวณว่าจะต้องใช้ปริมาณวัสดุเท่าใด ราคาวัสดุทั้งหมดเท่าไหร่สำหรับงานนี้ </p><p><strong> ภายในโปรแกรมต้องมีฟังก์ชันดังต่อไปนี้ </strong></p><ul><li><span style="color:red;"><code>inputShape()</code></span> สำหรับรับค่า และ คืนค่า<strong>ข้อมูลนำเข้าที่รับมา เพียงค่าเดียว</strong>ซึ่งเป็นตัวเลขระบุว่าต้องสร้างเป็นรูปทรงอะไร โดยข้อมูลนำเข้าประกอบด้วยหมายเลข 1 (ทรงกลม) 2 (ทรงกรวย) 3 (ทรงกระบอก) 4 (ปริซึมฐานสี่เหลี่ยม) 5 (พีระมิดฐานสี่เหลี่ยม) เพื่อนำไปหาต่อว่าต้องคำนวณด้วยฟังก์ชันใด</li><li><span style="color:red;"> calculateSphere() </span> สำหรับรับค่ารัศมี คำนวณ แสดงผล และ คืนค่าปริมาตรทรงกลม</li><li><span style="color:red;"> calculateCone() </span> สำหรับรับค่ารัศมี,ความสูง  คำนวณ แสดงผล และ คืนค่าปริมาตรทรงกรวย</li><li><span style="color:red;"> calculateCylinder() </span> สำหรับรับค่ารัศมี,ความสูง คำนวณ แสดงผล และ คืนค่าปริมาตรทรงกระบอก</li><li><span style="color:red;"> calculatePrism() </span> สำหรับรับค่าความกว้าง,ยาว,สูง คำนวณ แสดงผล และ คืนค่าปริมาตรปริซึมฐานสี่เหลี่ยม (Rectangular prisms) </li><li><span style="color:red;"> calculatePyramid() </span> สำหรับรับค่าความกว้าง,ยาว,สูง คำนวณ แสดงผล และ คืนค่าปริมาตรพีระมิดฐานสี่เหลี่ยม (Rectangle-based pyramids) <strong>ให้ใช้สูตร กว้าง * ยาว * สูง / 3 เท่านั้น ห้ามใช้ (1/3) * กว้าง * ยาว * สูง </strong></li><li><span style="color:red;"> calculatePrice(v) </span> สำหรับรับค่าราคาต่อ 1 ลบ.ม. คำนวณและแสดงผลราคาของวัสดุ</li></ul><p><strong> สามารถดูส่วนประกอบต่างๆภายในฟังก์ชันดังตัวอย่าง </strong></p><p><strong>กำหนดให้ค่า pi = 3.141592653589793 </strong></p><p><strong>ให้ใช้ตัวแปรเป็น int ทุกตัว</strong></p><p><strong>ข้อมูลส่งออกทุกค่าเป็นทศนิยม 2 ตำแหน่ง</strong></p><p><a href="https://www.khanacademy.org/math/geometry/hs-geo-solids/hs-geo-solids-intro/a/volume-formulas-review?fbclid=IwAR3e3wSOwdkp3EvCCEROLsbimrFc1rc_1jBnskGbYCQmy8C0WY8Dkyv5p7o" target="_blank"> สูตรการหาปริมาตรรูปทรงต่าง ๆ (คลิ๊ก) </a></p><h2>Example 1</h2><p></p><pre class="output">Input Shape: <em>1</em>
Input radius(meter): <em>5</em>
The volume is <strong>523.60</strong> cubic meter.
Price(Bath) per 1 cubic meter: <em>2</em>
The price is <strong>1047.20</strong> Baht.
</pre><p></p><h2>Example 2</h2><p></p><pre class="output">Input Shape: <em>2</em>
Input radius(meter): <em>3</em>
Input height(meter): <em>4</em>
The volume is <strong>37.70</strong> cubic meter.
Price(Bath) per 1 cubic meter: <em>5</em>
The price is <strong>188.50</strong> Baht.
</pre><p></p><h2>Example 3</h2><p></p><pre class="output">Input Shape: <em>3</em>
Input radius(meter): <em>4</em>
Input height(meter): <em>5</em>
The volume is <strong>251.33</strong> cubic meter.
Price(Bath) per 1 cubic meter: <em>6</em>
The price is <strong>1507.96</strong> Baht.
</pre><p></p><h2>Example 4</h2><p></p><pre class="output">Input Shape: <em>4</em>
Input width(meter): <em>4</em>
Input length(meter): <em>2</em>
Input height(meter): <em>2</em>
The volume is <strong>16.00</strong> cubic meter.
Price(Bath) per 1 cubic meter: <em>10</em>
The price is <strong>160.00</strong> Baht.
</pre><p></p><h2>Example 5</h2><p></p><pre class="output">Input Shape: <em>5</em>
Input width(meter): <em>6</em>
Input length(meter): <em>3</em>
Input height(meter): <em>4</em>
The volume is <strong>24.00</strong> cubic meter.
Price(Bath) per 1 cubic meter: <em>2</em>
The price is <strong>48.00</strong> Baht.
</pre><p></p><p></p><fieldset><pre><div class="code-menu"><a href="#" class="lineno-toggle">[hide line #]</a></div><code class="source"><textarea class="codeblank" cols="63" name="b1" rows="57" wrap="off" autocomplete="off"></textarea></code></pre></fieldset><p></p><p></p><p>และน้องๆ ได้ความรู้อะไรบ้างจากการทำโจทย์ข้อนี้</p><p><input class="textblank" name="b2" size="76" type="text" value=""></p> 
      </div>
      
      
    </form>
  </div>