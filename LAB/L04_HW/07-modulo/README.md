<div id="current" aria-labelledby="ui-id-29" role="tabpanel" class="ui-tabs-panel ui-corner-bottom ui-widget-content" aria-hidden="false">
    <form method="post" action="/elab/lab/submit/1023/11635/19099/" enctype="multipart/form-data" autocomplete="off">
      <div id="assignment-body">
        <input type="hidden" name="csrfmiddlewaretoken" value="9N5025yDViwae4M8IujT76HWjlCvdHzUypt7t2MWbVYZmIxzyCEWbswWl3DBVMPu">
        <h1>modulo หารเอาเศษ</h1><p>กำหนดจำนวนเต็ม A และ  B เมื่อ A modulo B จะได้ผลลัพธ์เป็นเศษจากการหาร A ด้วย B เช่น 7,14,27,38 เมื่อ modulo ด้วย 3 จะได้ผลลัพธ์เป็น 1,2,0 และ 2 ตามลำดับ </p><p>ให้เขียนโปรแกรมรับจำนานเต็ม N จำนวน จากนั้นทำการ modulo แต่ละจำนวณด้วย M </p><p>จากนั้นจะพบว่าผลลัพท์ในการ modulo แต่ละครั้งอาจจะเท่ากันหรือไม่เท่ากันก็ได้ จึงให้หาว่า จากจำนวนทั้ง N จำนวนนั้น มีผลลัพท์ที่แตกต่างกันได้กี่แบบ</p><p>เช่น มีจำนวน คือ 5 6 7 8 9 ทำการ modulo ด้วย 3 ได้ผลคือ 2 0 1 2 0 จะพบว่ามีผลลัพท์ที่แตกต่างกันแค่ 3 แบบ คือ 0 1 2 จึงได้ 3 แบบเป็นคำตอบ</p><h2>Example 1</h2><p></p><pre class="output">N: <em>10</em>
M: <em>42</em>
Input number 1: <em>1</em>
Input number 2: <em>2</em>
Input number 3: <em>3</em>
Input number 4: <em>4</em>
Input number 5: <em>5</em>
Input number 6: <em>6</em>
Input number 7: <em>7</em>
Input number 8: <em>8</em>
Input number 9: <em>9</em>
Input number 10: <em>10</em>
10
</pre><p></p><h2>Example 2</h2><p></p><pre class="output">N: <em>10</em>
M: <em>42</em>
Input number 1: <em>39</em>
Input number 2: <em>40</em>
Input number 3: <em>41</em>
Input number 4: <em>42</em>
Input number 5: <em>43</em>
Input number 6: <em>44</em>
Input number 7: <em>82</em>
Input number 8: <em>83</em>
Input number 9: <em>84</em>
Input number 10: <em>85</em>
6
</pre><p></p><h2>Example 3</h2><p></p><pre class="output">N: <em>15</em>
M: <em>10</em>
Input number 1: <em>10</em>
Input number 2: <em>20</em>
Input number 3: <em>30</em>
Input number 4: <em>40</em>
Input number 5: <em>50</em>
Input number 6: <em>60</em>
Input number 7: <em>70</em>
Input number 8: <em>80</em>
Input number 9: <em>90</em>
Input number 10: <em>100</em>
Input number 11: <em>120</em>
Input number 12: <em>130</em>
Input number 13: <em>140</em>
Input number 14: <em>1000</em>
Input number 15: <em>10</em>
1
</pre><p></p><p>Note:   จาก Example 1 1%42 = 1, 2%42 = 2,..., 10%42 = 10 ดังนั้นจึงมีเศษทั้งหมด 10 รูปแบบ<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;จาก Example 2 มีเศษจากการหารด้วย 42 ทั้งหมด 6 รูปแบบนั่นคือ 0(42,84), 1(43,85), 2(44), 39(39), 40(40,82), 41(41,83)</p><p></p><fieldset><pre><div class="code-menu"><a href="#" class="lineno-toggle">[hide line #]</a></div><code class="source"><textarea class="codeblank" cols="54" name="b1" rows="15" wrap="off" autocomplete="off"></textarea></code></pre></fieldset><p></p> 
      </div>
      
      
    </form>
  </div>