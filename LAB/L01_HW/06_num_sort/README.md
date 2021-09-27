<div id="current" aria-labelledby="ui-id-21" role="tabpanel" class="ui-tabs-panel ui-corner-bottom ui-widget-content" aria-hidden="false">
    <form method="post" action="/elab/lab/submit/1023/11538/19000/" enctype="multipart/form-data" autocomplete="off">
      <div id="assignment-body">
        <input type="hidden" name="csrfmiddlewaretoken" value="HlQGsJeK4rk29FesC66GH6Oba85IFUcy6XeNTGs3k4MRhjZTserJLsDbcQ6OnZs8">
        <h1>4_num_sort : เรียงเลข 4 ตัว</h1><p>จงเขียนโปรแกรมรับค่าตัวเลขจำนวนเต็ม 4 จำนวน </p><p>แล้วให้แสดงเลขทั้ง 4 จำนวน โดยเรียงจากน้อยไปหามาก</p><p><strong>ห้ามใช้ฟังก์ชัน sort() หรือ sorted() หรือฟังก์ชันเสริมใดๆ ในการช่วยเรียงข้อมูลโดยเด็ดขาด</strong> </p><p><strong>ห้ามประกาศ list หรือ โครงสร้างข้อมูลใดๆ ในการเก็บข้อมูล</strong> </p><p><strong>ห้ามใช้ build-in function เช่น min() max()</strong> </p><p><strong>และไม่อนุญาติให้นิสิตนิยามฟังก์ชั่นเรียงข้อมูลด้วยตนเอง เช่น selection sort , bubble sort เป็นต้น</strong></p><p><strong>หากตรวจพบ คุณจะไม่ได้คะแนนในข้อนี้</strong></p><p><strong>FYI</strong> : ในส่วนของการรับค่าและแสดงผล ไม่ต้องเขียนลงมาในช่องสีเหลือง ให้น้องเขียนโปรแกรม
ที่สามารถทำให้ตัวแปร one two three four มีค่าที่ถูกต้องตามที่โจทย์ต้องการเท่านั้น</p><h2>Example1</h2><p></p><pre class="output"><em>2 4 3 1</em>
1 2 3 4
</pre><p></p><p></p><fieldset><pre><div class="code-menu"><a href="#" class="lineno-toggle">[hide line #]</a></div><code class="source">a,b,c,d <span class="o">=</span> <span class="nb">map</span>(<span class="nb">int</span>,<span class="nb">input</span>()<span class="o">.</span>split())
one,two,three,four <span class="o">=</span> <span class="mi">0</span>,<span class="mi">0</span>,<span class="mi">0</span>,<span class="mi">0</span>
</code></pre></fieldset>
<fieldset><pre><div class="code-menu"><a href="#" class="lineno-toggle">[hide line #]</a></div><code class="source"><textarea class="codeblank" cols="45" name="b1" rows="24" wrap="off" autocomplete="off"></textarea></code></pre></fieldset>
<fieldset><pre><div class="code-menu"><a href="#" class="lineno-toggle">[hide line #]</a></div><code class="source"><span class="nb">print</span>(f<span class="s1">'</span><span class="si">{one}</span><span class="s1"> </span><span class="si">{two}</span><span class="s1"> </span><span class="si">{three}</span><span class="s1"> </span><span class="si">{four}</span><span class="s1">'</span>)
</code></pre></fieldset><p></p><p><u><strong>Hint</strong></u><strong> :</strong> ลองเรียงเฉพาะ 3 ตัวก่อน </p><p>และน้องๆ ได้ความรู้อะไรบ้างจากการทำโจทย์ข้อนี้</p><p><input class="textblank" name="b2" size="76" type="text" value=""></p> 
      </div>
      
      
    </form>
  </div>