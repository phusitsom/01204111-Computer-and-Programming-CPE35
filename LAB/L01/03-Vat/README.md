<div id="assignment-body">
        <input type="hidden" name="csrfmiddlewaretoken" value="PbhuOaY8yS7r4aeH6jbOYM83XfQ0jV5peNFBf7crOvzgcOZ8WrwR28X3ZXR610lZ">
        <h1>Vat</h1><p>เวลาเราไปร้านอาหารนั้น เราก็จะต้องจ่ายภาษีเพิ่มขึ้นจากค่าอาหารเดิมเป็นจำนวน 7% โดยที่เราก็ไม่รู้เลยว่าร้านอาหารนั้นคิดถูกหรือผิด </p><p>เนื่องจากน้องๆเก่งทางด้านเขียนโปรแกรม พี่ๆจึงอยากให้น้องเขียนโปรแกรมรับจำนวนเงินที่รวมภาษีแล้ว</p><p>นำมาคำนวณว่าในจำนวนเงินนั้นเป็นค่าอาหารจริงกี่บาท และภาษีกี่บาท</p><p><strong>ให้หาค่าภาษีจาก ภาษี = ราคารวมภาษี - ราคาไม่รวมภาษี</strong></p><p><strong>เนื่องจากโจทย์ไม่สามารถ format float ได้ ขอให้น้องหาค่า ราคาไม่รวมภาษี จาก ราคา = ราคารวมภาษี /107 *100 </strong></p><h2>Example 1</h2><p></p><pre class="output">summary price : <em>107</em>
food : 100.0
vat : 7.0
</pre><p></p><h2>Example 2</h2><p></p><pre class="output">summary price : <em>3265</em>
food : 3051.4018691588785
vat : 213.59813084112147
</pre><p></p><h2>Example 3</h2><p></p><pre class="output">summary price : <em>152.9</em>
food : 142.89719626168224
vat : 10.002803738317766
