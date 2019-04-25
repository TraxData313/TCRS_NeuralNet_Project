# Research Description:
<p><b>The problem</b>:</p>
&nbsp;&nbsp;&nbsp; Neural Networks (NNs) and Conventional Computers (CCs) are separate types of Input/Output Machines (IOMs), but yet every NN only successfully exists as a simulation in a CC.<br>
&nbsp;&nbsp;&nbsp; Most of the research today is concentrated at optimizing the NNs to be a better fit for the CCs, or making the CCs a better host for the NNs.
<br>
<br>
<p><b>The motivation</b>:</p>
- I believe that we need to "free" the NNs, if we want to achieve the success of the CCs.
- If we build the NNs in a "smart" way that will no longer need our CCs to carry out the heavy tast of optimizing them, but as to outsource that job to the laws of nature, we can stop finding ways to build ligther optimization tasks, but start working on making smaller neurons, making faster connections... Start the process of scaling the number of neurons in the networks as fast as how we were/are scaling the number of transistors in our computers, achieve the Moore's Law of NNs.

<b>The conjecture</b>:
- The main obstruction is the Global nature of the current successful optimization (learning) algorithms. We state the optimization problem as a system of linear equations to make it easier for the CC and then compromise and polish out edges.
- But in general, to optimize a weight, one needs to ask the CC to compute a function, having in mind the relation of that one weight with respect to all others. And then the CC needs to do this for all weights.
- If the Global nature of the process is the obstruction, the solution would be to make a Local process, Local rules that every part of the NN will follow and of which the Learning, Optimization and Intellect will be able naturally emerge.
<b>Personal notes</b>:
- This is what this research is about, and in the section below I'll be tracking its progress.
- Why I work on this - I think we'll need the best symmetry extractor if we are to start braking the problem of extracting all the symmetrys in nature.
<br><br>
 
# Reseach Progress:
<p></p>
<b>The Static Covariant Feedback System</b>:
<p></p>
> The Static Covariant Feedback System is an ANN-like Logistic Regression System.<br>
> It uses a Local "covariant" learning algorithm that independently updates weights between the cells (bit holders).<br>
> With no hidden layers, the system can perform Logistic Regression of any N independent inputs, like classifing a point given N coordinates.<br>
> With a few hidden layers, the system can learn to perform harder Classifier tasks, like predicting whether a Bank customer will Churn.<br>
<br>
<p></p>
<b>The Predictor System</b>:
<p></p>
> The Predictor System is a CNN-like Continuous Regression System.<br>
> It takes "timestamps" of continuous data, like stock prices, and predicts the values for the next N timestamps (future prices).<br>
> The learning algorithm is Local, similar to the one used in the Static Covariant Feedback System, but the Cell-to-Cell connections are static (constant weights), and instead every cell uses covariant connection to the newest input.<br>
> Every cell then makes independent prediction, and the final prediction is a weighted sum of the cell predictions, with the weights beeing the Ratings that each cell has. Then the system simulates itself, using the newest prediction as input, to predict the next future value and repeats this process for N times in order to give N future predictions. Once the new, real value comes, every cell check the prediction it made to update its own Rating.<br>


<br><br><br>
- Not sure if I need to add this or if it ever be red, but here it it:
<p><em>Disclaimer:</em></p>
<blockquote>
<p>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</p>
</blockquote>
