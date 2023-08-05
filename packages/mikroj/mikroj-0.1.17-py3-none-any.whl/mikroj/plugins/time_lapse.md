---
id: time_lapse_color_coder
title: Time-Lapse Color Coder
sidebar_label: Real-Time Monitoring
slug: /
code_parser: groovy
definition_parser: yaml, meta
actor: stacktostack
version: 1.0
template: no
---

## Introduction 
Coming back to our original example.

You have three computers in your lab, each equipped with one essential equipment for your analysis flow:

1. Machine A  is the Microscope with some organoid samples.
2. Machine B is your Deep-Learning workstation, without any display.
3. Machine C is your personal Computer with ImageJ installed.

You want to sequentially acquire an image from your microscope, segment it in your deep learning workstation and then display the result on Napari in your office.

Of course you can call of this steps sequentially.

```yaml
args:
- description: The color coded Image
  identifier: representation
  key: rep
  label: null
  transpile: null
  typename: StructureArgPort
  widget: 
	typename: SearchWidget
	query: 
description: Color Code an Iamge
interface: color_code_image
kwargs: []
name: Color Code Image
package: test
returns:
- description: The color coded Image
  identifier: representation
  key: rep
  label: null
  transpile: null
  typename: StructureReturnPort
type: FUNCTION
typename: Node
```


``` groovy

var Glut = "Fire";	//default LUT
var Gstartf = 1;
var Gendf = 10;
var GFrameColorScaleCheck = 1;
var GbatchMode = 0;

macro "Time-Lapse Color Coder" {
Stack.getDimensions(ww, hh, channels, slices, frames);
if (channels > 1)
	exit("Cannot color-code multi-channel images!");
//swap slices and frames in case:
if ((slices > 1) && (frames == 1)) {
	frames = slices;
	slices = 1;
	Stack.setDimensions(1, slices, frames);
	print("slices and frames swapped");
}
Gendf = frames;
if (Gstartf <1) Gstartf = 1;
if (Gendf > frames) Gendf = frames;
totalframes = Gendf - Gstartf + 1;
calcslices = slices * totalframes;
imgID = getImageID();

setBatchMode(true);

newImage("colored", "RGB White", ww, hh, calcslices);
run("Stack to Hyperstack...", "order=xyczt(default) channels=1 slices="
	+ slices + " frames=" + totalframes + " display=Color");
newimgID = getImageID();

selectImage(imgID);
run("Duplicate...", "duplicate");
run("8-bit");
imgID = getImageID();

newImage("stamp", "8-bit White", 10, 10, 1);
run(Glut);
getLut(rA, gA, bA);
close();
nrA = newArray(256);
ngA = newArray(256);
nbA = newArray(256);

newImage("temp", "8-bit White", ww, hh, 1);
tempID = getImageID();

for (i = 0; i < totalframes; i++) {
	colorscale = floor((256 / totalframes) * i);
	for (j = 0; j < 256; j++) {
		intensityfactor = j / 255;
		nrA[j] = round(rA[colorscale] * intensityfactor);
		ngA[j] = round(gA[colorscale] * intensityfactor);
		nbA[j] = round(bA[colorscale] * intensityfactor);
	}

	for (j = 0; j < slices; j++) {
		selectImage(imgID);
		Stack.setPosition(1, j + 1, i + Gstartf);
		run("Select All");
		run("Copy");

		selectImage(tempID);
		run("Paste");
		setLut(nrA, ngA, nbA);
		run("RGB Color");
		run("Select All");
		run("Copy");
		run("8-bit");

		selectImage(newimgID);
		Stack.setPosition(1, j + 1, i + 1);
		run("Select All");
		run("Paste");
	}
}

selectImage(tempID);
close();

selectImage(imgID);
close();

selectImage(newimgID);

run("Stack to Hyperstack...", "order=xyctz channels=1 slices="
	+ totalframes + " frames=" + slices + " display=Color");
op = "start=1 stop=" + Gendf + " projection=[Max Intensity] all";
run("Z Project...", op);
if (slices > 1)
	run("Stack to Hyperstack...", "order=xyczt(default) channels=1 slices=" + slices
		+ " frames=1 display=Color");
resultImageID = getImageID();

selectImage(newimgID);
close();

selectImage(resultImageID);

if (GbatchMode == 0)
	setBatchMode("exit and display");
}


```

