<div id="current" aria-labelledby="ui-id-41" role="tabpanel" class="ui-tabs-panel ui-corner-bottom ui-widget-content" aria-hidden="false">
    <form method="post" action="/elab/lab/submit/1023/11635/19109/" enctype="multipart/form-data" autocomplete="off">
      <div id="assignment-body">
        <input type="hidden" name="csrfmiddlewaretoken" value="m7P740vc4EaE2uZ4gsvxUN8SbYYHBEmsLJdevXJvkhCta8Kv6AQAY9XSdGZNjJC2">
        <h1>charPicGrid</h1><p>กำหนดให้ grid1, grid2 เป็น list 2 มิติ ตามด่านล่าง (ให้นิสิตนำไปใส่ในโค้ดด้วย)
</p><pre class="output">grid1 = [['.','.','.','.','.','.'],
        ['.','o','o','.','.','.'],
        ['o','o','o','o','.','.'],
        ['o','o','o','o','o','.'],
        ['.','o','o','o','o','o'],
        ['o','o','o','o','o','.'],
        ['o','o','o','o','.','.'],
        ['.','o','o','.','.','.'],
        ['.','.','.','.','.','.']]
</pre><p></p><pre class="output">grid2 = [['.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.'],
        ['.','.','.','.','o','.','o'],
        ['o','o','.','o','.','o','.'],
        ['o','o','o','o','o','.','.'],
        ['o','o','.','o','.','o','.'],
        ['.','.','.','.','o','.','o'],
        ['.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.']]
</pre>
<p>ในนิสิตสร้าง function ดังนี้<br> </p><ul> <strong>rotate_lerft(grid)</strong> ทำหน้าที่ในการหมุนรูปไปทางซ้าย 90 องศา <em>return list 2 มิติ</em></ul> 
 <ul> <strong>rotate_right(grid)</strong> ทำหน้าที่ในการหมุนรูปไปทางขวา 90 องศา <em>return list 2 มิติ</em></ul>
 <ul> <strong>print_grid(grid)</strong> ทำหน้าที่ในการ print grid  </ul><p></p><h2>Examples 1 (shell mode)</h2><p></p><pre class="output"><span class="console">&gt;&gt;&gt; </span><span class="stdin"><em>grid = rotate_right(grid1)</em></span>
<span class="console">&gt;&gt;&gt; </span><span class="stdin"><em>print_grid(grid)</em></span>
..oo.oo..
.ooooooo.
.ooooooo.
..ooooo..
...ooo...
....o....
</pre><p></p><h2>Examples 2 (shell mode)</h2><p></p><pre class="output"><span class="console">&gt;&gt;&gt; </span><span class="stdin"><em>grid = rotate_left(grid1)</em></span>
<span class="console">&gt;&gt;&gt; </span><span class="stdin"><em>print_grid(grid)</em></span>
....o....
...ooo...
..ooooo..
.ooooooo.
.ooooooo.
..oo.oo..
</pre><p></p><h2>Examples 3 (shell mode)</h2><p></p><pre class="output"><span class="console">&gt;&gt;&gt; </span><span class="stdin"><em>print_grid(rotate_right(grid2))</em></span>
...ooo...
...ooo...
....o....
...ooo...
..o.o.o..
...o.o...
..o...o..
</pre><p></p><h2>Examples 4 (shell mode)</h2><p></p><pre class="output"><span class="console">&gt;&gt;&gt; </span><span class="stdin"><em>print_grid(rotate_right(rotate_left(rotate_left(grid2))))</em></span>
..o...o..
...o.o...
..o.o.o..
...ooo...
....o....
...ooo...
...ooo...
</pre><p></p><h1 style="color:Tomato;"> "หากพบว่ามีการคัดลอกโค้ดเกิดขึ้น จะดำเนินการตามระเบียบของมหาวิทยาลัย" </h1>
<p></p><fieldset><pre><div class="code-menu"><a href="#" class="lineno-toggle">[hide line #]</a></div><code class="source"><textarea class="codeblank" cols="52" name="b1" rows="46" wrap="off" autocomplete="off"></textarea></code></pre></fieldset><p></p><p></p> 
      </div>
      
      
    </form>
  </div>