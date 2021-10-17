<template>
  <v-container>
    <v-row>
      <v-col>
        <h1>About</h1>
        <h2>DSK method</h2>
        <p>You need to find the interval [<strong><em>a<sub>0</sub>, b</em></strong><sub><strong><em>0</em></strong></sub>] on which the point <strong><em>x<sup>*</sup></em></strong> is located. This method is used for one-dimensional minimization. The DSK method seeks the initial localization of the minimum of the unimodal function, ie a simple one-dimensional search with doubling of the step, the end criterion of which is the appearance of a sign of the growth of the function. Consider the algorithm for finding the interval at which there is a minimum.</p>
        <ol>
          <li>The input parameters will be: <strong><em>f(x)</em></strong> - goal function, <strong><em>x</em></strong><sub><strong><em>0</em></strong>&nbsp;</sub> and step <strong><em>h</em></strong><sub><strong><em>0</em></strong>&nbsp;</sub> &gt; 0;</li>
          <li>Calculate the values of&nbsp;<strong><em>f(x<sub>0</sub>)</em></strong>,&nbsp;<strong><em>f(x<sub>0</sub> + h<sub>0</sub>)</em></strong>,&nbsp;<strong><em>k = 0;</em></strong></li>
          <li>If <strong><em>f(x<sub>0</sub>) &lt; f(x<sub>0</sub> + h<sub>0</sub>)&nbsp;</em></strong>then in the given step we change a sign<strong><em>: h<sub>0</sub> = -h<sub>0</sub>,&nbsp;</em></strong>otherwise we leave that is.</li>
          <li>While&nbsp;<strong><em>f(x<sub>0</sub>) &gt; f(x<sub>0</sub> + h<sub>0</sub>)</em></strong>, then&nbsp;<strong><em>x<sub>k+1</sub> = x<sub>k</sub> + h<sub>k</sub> , h<sub>k+1</sub> = 2h<sub>k</sub> ,&nbsp;k = k + 1</em></strong>.</li>
          <li>Find the points: <strong><em>x<sub>k + 1</sub> = x<sub>k</sub> + h<sub>k</sub> = x<sub>m</sub>,&nbsp;x<sub>k</sub> = x<sub>m-1</sub>, x<sub>k-1</sub> = x<sub>m-2</sub></em></strong>.</li>
          <li>Next, reduce the step <strong><em>h<sub>k + 1</sub> = h<sub>k</sub> / 2</em></strong>&nbsp;and calculate <strong><em>x<sub>m + 1</sub> = x<sub>m&nbsp;</sub>- h</em></strong><sub><strong><em>k + 1</em></strong></sub>.</li>
          <li>We look for the value of the function at all points found. The point at which the value of the function is greatest (<strong><em>x</em></strong><sub><strong><em>m</em></strong></sub> or <strong><em>x</em></strong><sub><strong><em>m-2</em></strong></sub>) is removed.</li>
        </ol>
        <p>Thus, we have three points left - they form a localized segment with an inner point.</p>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <h2>Golden ratio</h2>
        <p>Algorithm</p>
        <ol>
          <li>Specify the initial localized segment [<strong><em>a<sub>0</sub>,b</em></strong><sub><strong><em>0</em></strong></sub>], accuracy of calculations <strong><em>&epsilon; &gt; 0, k=0</em></strong>;</li>
          <li>Calculate <strong><em>y<sub>k</sub> = a<sub>k</sub> + <v-math formula="$\boldsymbol{\frac{3 - \sqrt{5}}{2}(b_{k} - a_{k})}$"/>, z<sub>k</sub> = a<sub>k</sub> + <v-math formula="$\boldsymbol{\frac{\sqrt{5} - 1}{2}(b_{k} - a_{k})}$"/> = a<sub>k</sub> + b<sub>k</sub> - y</em></strong><sub><strong><em>k</em></strong>&nbsp;&nbsp;</sub>and the value of the function at these points&nbsp;<strong><em>f(y<sub>k</sub>),&nbsp;f(z<sub>k</sub>)</em></strong>.</li>
          <li>Define a new localized segment. If <strong><em>f(y<sub>k</sub>) &le; f(z<sub>k</sub>)</em></strong>&nbsp;
          &nbsp; &nbsp;then <strong><em>a<sub>k+1</sub> = a<sub>k</sub></em></strong>, <strong><em>b<sub>k+1</sub> = z<sub>k</sub></em></strong>, <strong><em>z<sub>k+1</sub> = y<sub>k</sub></em></strong>, <strong><em>y<sub>k+1</sub> = a<sub>k+1</sub> + b<sub>k+1</sub> - z<sub>k+1</sub></em></strong> and go to step 4,
          &nbsp; &nbsp;otherwise put <strong><em>a<sub>k+1</sub> = y</em></strong><sub><strong><em>k</em></strong></sub>, <strong><em>b<sub>k+1</sub> = b</em></strong><sub><strong><em>k</em></strong></sub>, <strong><em>y<sub>k+1</sub> = z</em></strong><sub><strong><em>k</em></strong></sub>,<strong><em>&nbsp;z<sub>k+1</sub> = a<sub>k+1</sub> + b<sub>k+1</sub> - y</em></strong><sub><strong><em>k+1</em></strong></sub> and go to step 4.</li>
          <li>If <strong><em>|a<sub>k+1</sub> - b<sub>k+1</sub>| &le; &epsilon;</em></strong>, the search is complete.</li>
        </ol>
        <p>You can take the middle of the interval as an approximate solution <v-math formula="$\boldsymbol{x^{*} \cong \frac{a_{k+1} + b_{k+1}}{2}}$"/></p>
        <p>otherwise, put <strong><em>k = k + 1</em></strong> and go to step 2.</p>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <h2>Piecewise Functions</h2>
        <ul>
          <li><b>Min</b>, <b>Max</b> — min and max</li>
          <li><b>RealAbs</b> — absolute value</li>
          <li><b>Piecewise</b> — general piecewise function</li>
        </ul>
        <h3>Exponential Functions</h3>
        <ul>
          <li><b>Log</b> — base-e logarithm (Log[b,x] uses base b)</li>
          <li><b>Log10, Log2</b> — base-10, base-2 logarithms</li>
          <li><b>Exp</b> — exponential</li>
          <li><b>Power (^)</b> — power (entered as a superscript using)</li>
          <li><b>Sqrt</b> — square root (entered using)</li>
          <li><b>CubeRoot, Surd</b> — real-number fractional powers</li>
        </ul>
          <h3>Trigonometric Functions</h3>
        <b>Degree (°)</b> — constant for converting to degrees <br>

        Sin ▪  Cos ▪  Tan<br>

          ArcSin ▪  ArcCos ▪  ArcTan<br>

          Sinc<br>

        <h3>Hyperbolic Functions</h3>
          Sinh ▪  Cosh ▪  Tanh<br>

          ArcSinh ▪  ArcCosh ▪  ArcTanh<br>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import  {VueMathjax} from 'vue-mathjax';
export default {
  components: {
    'v-math': VueMathjax
  }
}
</script>
