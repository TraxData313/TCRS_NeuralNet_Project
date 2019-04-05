<p><em>Disclaimer:</em></p>
<blockquote>
<p>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</p>
</blockquote>


# CellNetworkBase details:
- Used Python 2.7
- The 3D design of the network of cells allows storage and update of memory, while allowing "flow of reactions" system to run layer-to-layer, taking into account present input, sored memory and predicted future
- The network design is optimized for real time streamed data processing - like analyzing human speech
- The network is used only to house the cells and their relative locations
- The cell-to-cell connection matrices and all the other properties are stored at cell level
- Localized connections allow for separate flows of data to be used to carry out combinations of different reactions, instead of propagating a single state


# The Cell Network is used to implement:
- Instead of standard gradient decent methods, every cell keeps track of the flow of information passing through it, which allows for a micro-ruled feedback system
- Specificly designed classifier selects groups of outputs, generating strategies (moving away from mere reactions). The "flow of reactions" system allows the actions to be carried out in time in order
- Standard covarience tracking would not work well, so optimized change-to-change system was invented to allow:
- - C-Pred system: calculation based future predictions
- - I-Pred system: intuition
- Prediction rating and optimization systems evolve better and better predictions over elapsed time


# To do:
- Many optimizations are needed, to name a few:
- - Building the two types of predictions requires copy of the whole cell-network, on which the future simulation takes over. I am working on a conjecture that the brain's dendride system may be the solution to this problem.
- - Optimize the code to run on GPU, keeping all rules cell-based.


# Usage:
- File "networkMod.py" contains the module
- File "testing.py" contains a sample test
- Download the two files and run the "testing.py" file, it will:
- - create a 10x10x10 Network instance and populate it with cells
- - start inputing information to the network and will print the cell values, layer-by-layer
- - you can change the input size or function (for example take stock prices as input)


- Contact = antongeorgiev313@gmail.com
