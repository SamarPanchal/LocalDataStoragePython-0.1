<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta http-equiv="Content-Style-Type" content="text/css">
  <title></title>
  <meta name="Generator" content="Cocoa HTML Writer">
  <meta name="CocoaVersion" content="2487.3">
  <style type="text/css">
    p.p1 {margin: 0.0px 0.0px 0.0px 0.0px; font: 13.0px Courier; color: #c37b59; background-color: #ffffff}
    p.p2 {margin: 0.0px 0.0px 0.0px 0.0px; font: 13.0px Courier; color: #afb1b7; background-color: #ffffff; min-height: 16.0px}
    p.p3 {margin: 0.0px 0.0px 0.0px 0.0px; font: 13.0px Courier; color: #afb1b7; background-color: #ffffff}
    p.p4 {margin: 0.0px 0.0px 0.0px 0.0px; font: 13.0px Courier; color: #599e5f; background-color: #ffffff; min-height: 16.0px}
    p.p5 {margin: 0.0px 0.0px 0.0px 0.0px; font: 13.0px Courier; color: #599e5f; background-color: #ffffff}
    span.s1 {color: #afb1b7}
    span.s2 {color: #c37b59}
    span.s3 {color: #a104a4}
    span.s4 {color: #803f7a}
    span.s5 {color: #599e5f}
    span.s6 {color: #4897f4}
    span.s7 {color: #7673ba}
    span.s8 {color: #5c6067}
  </style>
</head>
<body>
<p class="p1">import <span class="s1">os</span></p>
<p class="p2"><br></p>
<p class="p2"><br></p>
<p class="p3"><span class="s2">class </span>LocalDataStore:</p>
<p class="p3"><span class="Apple-converted-space">    </span><span class="s2">def </span><span class="s3">__init__</span>(<span class="s4">self</span>, file_type):</p>
<p class="p3"><span class="Apple-converted-space">        </span><span class="s4">self</span>.value = <span class="s2">None</span></p>
<p class="p3"><span class="s2"><span class="Apple-converted-space">        </span></span><span class="s4">self</span>.file_type = file_type</p>
<p class="p3"><span class="Apple-converted-space">        </span><span class="s2">if </span><span class="s4">self</span>.file_type == <span class="s5">''</span>:</p>
<p class="p3"><span class="Apple-converted-space">            </span><span class="s4">self</span>.file_type = <span class="s5">'txt'</span></p>
<p class="p4"><br></p>
<p class="p3"><span class="s5"><span class="Apple-converted-space">    </span></span><span class="s2">def </span><span class="s6">save_data</span>(<span class="s4">self</span>, filename):</p>
<p class="p3"><span class="Apple-converted-space">        </span><span class="s2">try</span>:</p>
<p class="p3"><span class="Apple-converted-space">            </span><span class="s2">with </span><span class="s7">open</span>(<span class="s7">str</span>(filename) + <span class="s5">"." </span>+ <span class="s7">str</span>(<span class="s4">self</span>.file_type), <span class="s5">'x'</span>) <span class="s2">as </span><span class="s8">f</span>:</p>
<p class="p3"><span class="Apple-converted-space">                </span><span class="s2">return True</span></p>
<p class="p1"><span class="Apple-converted-space">        </span>except <span class="s7">Exception </span>as <span class="s1">e:</span></p>
<p class="p3"><span class="Apple-converted-space">            </span><span class="s7">print</span>(e)</p>
<p class="p2"><br></p>
<p class="p3"><span class="Apple-converted-space">    </span><span class="s2">def </span><span class="s6">load_data</span>(<span class="s4">self</span>, filename):</p>
<p class="p3"><span class="Apple-converted-space">        </span><span class="s2">try</span>:</p>
<p class="p3"><span class="Apple-converted-space">            </span><span class="s2">with </span><span class="s7">open</span>(<span class="s7">str</span>(filename) + <span class="s5">"." </span>+ <span class="s7">str</span>(<span class="s4">self</span>.file_type), <span class="s5">'r'</span>) <span class="s2">as </span>f:</p>
<p class="p3"><span class="Apple-converted-space">                </span>data = f.read()</p>
<p class="p3"><span class="Apple-converted-space">                </span><span class="s2">return </span>data</p>
<p class="p3"><span class="Apple-converted-space">        </span><span class="s2">except </span><span class="s7">Exception </span><span class="s2">as </span>e:</p>
<p class="p3"><span class="Apple-converted-space">            </span><span class="s7">print</span>(e)</p>
<p class="p2"><br></p>
<p class="p3"><span class="Apple-converted-space">    </span><span class="s2">def </span><span class="s6">update_data</span>(<span class="s4">self</span>, filename, value):</p>
<p class="p3"><span class="Apple-converted-space">        </span><span class="s4">self</span>.value = value</p>
<p class="p3"><span class="Apple-converted-space">        </span><span class="s2">try</span>:</p>
<p class="p3"><span class="Apple-converted-space">            </span><span class="s2">with </span><span class="s7">open</span>(<span class="s7">str</span>(filename) + <span class="s5">"." </span>+ <span class="s7">str</span>(<span class="s4">self</span>.file_type), <span class="s5">'w'</span>) <span class="s2">as </span>f:</p>
<p class="p3"><span class="Apple-converted-space">                </span>f.write(value)</p>
<p class="p3"><span class="Apple-converted-space">        </span><span class="s2">except </span><span class="s7">Exception </span><span class="s2">as </span>e:</p>
<p class="p3"><span class="Apple-converted-space">            </span><span class="s7">print</span>(e)</p>
<p class="p2"><br></p>
<p class="p3"><span class="Apple-converted-space">    </span><span class="s2">def </span><span class="s6">delete_data</span>(<span class="s4">self</span>, filename):</p>
<p class="p3"><span class="Apple-converted-space">        </span><span class="s2">try</span>:</p>
<p class="p3"><span class="Apple-converted-space">            </span>os.remove(<span class="s7">str</span>(filename) + <span class="s5">"." </span>+ <span class="s7">str</span>(<span class="s4">self</span>.file_type))</p>
<p class="p3"><span class="Apple-converted-space">        </span><span class="s2">except </span><span class="s7">Exception </span><span class="s2">as </span>e:</p>
<p class="p3"><span class="Apple-converted-space">            </span><span class="s7">print</span>(e)</p>
<p class="p2"><br></p>
<p class="p2"><br></p>
<p class="p3"><span class="s2">if </span>__name__ == <span class="s5">'__main__'</span>:</p>
<p class="p5"><span class="s1"><span class="Apple-converted-space">    </span></span><span class="s7">print</span><span class="s1">(</span>"__init__ file"<span class="s1">)</span></p>
<p class="p2"><br></p>
</body>
</html>
