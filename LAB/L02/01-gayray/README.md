<div id="current" aria-labelledby="ui-id-1" role="tabpanel" class="ui-tabs-panel ui-corner-bottom ui-widget-content" aria-hidden="false" style="">
    <form method="post" action="/elab/lab/submit/1023/11543/19009/" enctype="multipart/form-data" autocomplete="off">
      <div id="assignment-body">
        <input type="hidden" name="csrfmiddlewaretoken" value="Ju3ssVAH1MvmywvuTPfoWlAhNMWxVKHp86rzTSO0hpXbGagVJXAr0HphPuXDDPXZ">
        <h1>เสาไฟกินรี 2 - เสาไฟใจเกเร</h1><p>จากข้อ <strong>เสาไฟกินรี 1 - corruption</strong> ทำให้เราสามารถคาดเดาได้แล้วว่าในโครงการนี้สร้างเสาไฟด้วยราคาเท่านี้จะมีการทุจริตไหม แต่เมื่อเราไปตรวจสอบจริงๆแล้ว กลับพบว่า เสาไฟแต่ละต้นที่ถูกสร้างในโครงการใดๆนั้น จะมีความสูงเท่ากัน <strong>แต่ราคาไม่เท่ากัน!!!</strong></p><p>เราจึงต้องตามไปสอบถามยังร้านหมูปิ้งซึ่งเป็นผู้รับเหมาโครงการว่า ทำไมราคาเสาไฟแต่ละต้นไม่เท่ากัน</p><p>ทางผู้รับเหมาได้ให้คำตอบกลับมาว่า เนื่องจากเสาไฟแต่ละต้นนั้นมีค่าแรงของแรงงานและวัสดุอุปกรณ์ที่ราคาปรับขึ้นๆลงๆ ทำให้ราคาแต่ละต้นไม่เท่ากัน</p><p>อีกทั้งทางผู้รับเหมายังมีการจ้าง<strong>คนงานใจเกเร</strong>ให้มาทำเสาไฟให้ในบางต้นด้วย ซึ่งคนงานใจเกเรนี้จะทำเสาไฟที่มีประสิทธิภาพทนทานและให้ความสว่างได้ยาวนานถึง 1 ปีแสงโดยที่ไม่ต้องหยุดพัก</p><p>และเราจะเรียกเสาไฟที่ถูกสร้างด้วยคนงานเหล่านี้ว่า <strong>เสาไฟใจเกเร</strong> แต่เนื่องจากเสาไฟใจเกเรมีต้นทุนที่สูงมากๆ ทำให้ผู้รับเหมาอาจจะใส่หรือไม่ใส่เข้าไปในโครงการก็ได้ ซึ่งถ้าหากจะใส่เอาไว้ก็จะใส่ไว้เพียง<strong>ต้นเดียว</strong>ต่อโครงการ</p><p>จากนั้นผู้รับเหมาก็ได้ให้วิธีคำนวณงบของโครงการวิธีใหม่ให้กับพวกเรา ซึ่งก่อนจะคำนวณงบรวมของโครงการได้นั้นจำเป็นต้องทราบเสียก่อนว่า ในโครงการนั้นมีเสาไฟใจเกเรอยู่หรือไม่ และเสาไฟใจเกเรที่มีอยู่นั้นราคาเท่าไหร่</p><p>จึงต้องไหว้วานให้เหล่า cpe35 ช่วยเขียนโปรแกรมเพื่อหาเสาไฟใจเกเรให้อีกนั่นเอง โดยเสาไฟใจเกเรจะมีเงื่อนไขของตัวมันอยู่ดังนี้</p><ol><li><p>เสาไฟใจเกเรจะเป็นเสาไฟที่มี<strong>ราคามากที่สุด</strong>ในโครงการ</p></li><li><p>เสาไฟใจเกเรจะต้องมี<strong>ราคาห่างจากเสาไฟต้นอื่น</strong>ที่มีราคามากที่สุด ตั้งแต่ <strong>3 เท่า</strong>เป็นต้นไป </p></li></ol><p>เช่น เสาไฟในโครงการทั้งหมด 4 ต้น มีราคา 50000, 15000, 12000, 9900 บาทตามลำดับ และพบว่าเสาไฟที่มีราคามากที่สุดนั้นมีราคามากกว่าเสาไฟที่มีราคารองลงมา เกิน 3 เท่า</p><p>50000 &gt; (15000*3) จึงนับได้ว่า โครงการนี้มีเสาไฟใจเกเร ราคา 50000 บาท</p><p><strong>ข้อมูลนำเข้า</strong></p><p>บรรทัดที่ 1 : จำนวนของเสาไฟฟ้าในโครงการ N ต้น (N เป็นเลขจำนวนเต็มที่มากกว่า 1)</p><p>บรรทัดที่ 2 ถึง N+1 : ราคาของเสาไฟฟ้าแต่ละต้น (เป็นเลขจำนวนเต็ม)</p><p><strong>ข้อมูลส่งออก</strong></p><p>บรรทัดที่ 1 : ผลว่ามีเสาไฟใจเกเรหรือไม่ ( YES : มี, NO : ไม่มี )</p><p><em>ถ้า มี เสาไฟใจเกเร</em> </p><p>บรรทัดที่ 2 : ราคาของเสาไฟใจเกเร (เป็นเลขจำนวนเต็ม)</p><h2>Example1</h2><p></p><pre class="output">number of electric poles : <em>4</em>
<em>50000</em>
<em>15000</em>
<em>12000</em>
<em>9900</em>
YES
50000
</pre><p></p><h2>Example2</h2><p></p><pre class="output">number of electric poles : <em>4</em>
<em>1250</em>
<em>1236</em>
<em>1100</em>
<em>1400</em>
NO
</pre><p></p><h2>Hint</h2><p></p><pre class="output">if cost &gt; max1:
   max2 = max1
   max1 = cost
elif cost &gt; max2:
   max2 = cost
/// max1 will &gt;= max2 all times
</pre><p></p><p></p><fieldset><pre><div class="code-menu"><a href="#" class="lineno-toggle">[hide line #]</a></div><code class="source"><textarea class="codeblank" cols="54" name="b1" rows="16" wrap="off" autocomplete="off"></textarea></code></pre></fieldset><p></p><p>และน้องๆ ได้ความรู้อะไรบ้างจากการทำโจทย์ข้อนี้</p><p><input class="textblank" name="b2" size="76" type="text" value=""></p> 
      </div>
      
      
    </form>
  </div>