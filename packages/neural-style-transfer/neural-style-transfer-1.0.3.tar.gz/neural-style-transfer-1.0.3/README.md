# neuralstyletransfer
This is the python library which takes two image *content image* and *style image* and provide the output image looks like 
a content image but painted in the style of provided reference style image

## Usage

```
python
from neuralstyletransfer.style_transfer import NeuralStyleTransfer
nst = NeuralStyleTransfer()
```
## Load the content image and style image from path
```
nst.LoadContentImage(content_img_path)
nst.LoadStyleImage(style_img_path)
```
### Use default parameters to train the model
### Default parameters are given below we can change it based on requirement by providing values on calling .apply method
- contentWeight=1e3
- styleWeight=1e-2
- epochs=300

```
output = nst.apply()
output.save('output.jpg')
```
