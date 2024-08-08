<h1>Image Encryptor/Decryptor</h1>
<p>A simple yet effective tool to encrypt and decrypt images using pixel-level RGB value inversion. This project was developed as part of my internship at Prodigy InfoTech, where I had the chance to explore the intersection of cybersecurity and image processing.</p>

<h2>Table of Contents</h2>
<ul>
<li>Introduction</li>
<li>Features</li>
<li>How It Works</li>
<li>Installation</li>
<li>Usage</li>
<li>GUI Version</li>
<li>CLI Version</li>

<h2>Introduction</h2>
<p>The Image Encryptor/Decryptor is a Python-based tool that allows users to encrypt and decrypt images by inverting the RGB values of each pixel. This approach provides a basic level of security, making it a great educational tool for those interested in learning about encryption techniques.</p>

<h2>Features</h2>
<ul><li>GUI Version:</li></ul> A user-friendly interface built with tkinter that simplifies the encryption and decryption process.
<ul><li>CLI Version:</li></ul> A straightforward command-line interface for quick processing.<br>
<ul><li>Symmetrical Encryption/Decryption:</li></ul> The same function is used for both encrypting and decrypting images, making the tool simple and efficient.
<h2>How It Works</h2>
<p>The core functionality of this tool is based on RGB value inversion. Each pixel's Red, Green, and Blue components are inverted (i.e., subtracted from 255). Applying this operation twice restores the original image, making decryption as simple as encryption.</p>

<h2>Installation</h2>
<p>To use this project, you'll need Python installed on your machine along with the Pillow library.</p>

<b>Install Pillow using pip:</b>


<code>pip install Pillow</code>
<h2>Usage</h2>
<h3>GUI Version</h3>
<ul>Run the Program:</ul>

<p>Simply run the image_encryptor_gui.py script using <code>python image_encryptor_gui.py</code>.</p>
<p>A window will open where you can browse for an image, select whether to encrypt or decrypt it, and choose the output path.</p>
<b><i>Encrypt or Decrypt:</i></b><br>

<p>Select the image you want to process.</p>
<p>Choose whether to encrypt or decrypt the image.</p>
<p>Specify where you'd like to save the processed image.</p>
<p>Click "Process" to execute the action.</p>
<h3>CLI Version</h3>
<ul>Run the Program:</ul>
<p>Run the image_encryptor_cli.py script in your terminal using <code>python image_encryptor_cli.py</code>.</p>
<b>Follow the Prompts:</b>
<p>Enter the path to the image you want to encrypt/decrypt.</p>
<p>Choose whether to encrypt or decrypt the image.</p>
<p>Provide the path where the processed image should be saved.</p>
