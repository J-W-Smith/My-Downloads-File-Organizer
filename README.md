<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>

<h1>File Organizer</h1>

<p>A Python script that organizes files in a directory based on their file extensions into categorized folders.</p>

<h2>Description</h2>

<p>This script categorizes files based on their file extensions and moves them into specific directories. This helps in organizing a messy directory by grouping files of similar types into separate folders.</p>

<h2>Features</h2>

<ul>
    <li><strong>Automatic Organization:</strong> Scan the current directory and organize files into respective folders.</li>
    <li><strong>Extensible:</strong> Easily extendable to support more file formats and directories.</li>
    <li><strong>Simple:</strong> Lightweight and straightforward script to organize files efficiently.</li>
</ul>

<h2>Directories and File Formats Supported</h2>

<p>Here's a breakdown of directories and file formats supported:</p>

<ul>
    <li><strong>AI:</strong> .safetensors</li>
    <li><strong>HTML:</strong> .html5, .html, .htm, .xhtml</li>
    <li><strong>IMAGES:</strong> .jpeg, .jpg, .tiff, .gif, .bmp, .png, .bpg, .svg, .heif, .psd, .jfif</li>
    <li><strong>VIDEOS:</strong> .avi, .flv, .wmv, .mov, .mp4, .webm, .vob, .mng, .qt, .mpg, .mpeg, .3gp</li>
    <!-- Add more as needed -->
</ul>

<h2>Usage</h2>

<ol>
    <li>Clone the repository or download the script.</li>
    <li>Navigate to the directory containing the script.</li>
    <li>Run the script using the command:</li>
</ol>

<pre><code>python script_name.py</code></pre>

<h2>How it Works</h2>

<p>The script utilizes Python's <code>os</code> and <code>pathlib</code> libraries to scan the current directory. It matches files based on their file extensions to predefined directories. Once matched, the script moves the file into the respective directory.</p>

<h2>Contributions</h2>

<p>Contributions are welcome! Feel free to open issues or submit pull requests to enhance the functionality or add new features.</p>

<h2>License</h2>

<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
</html>
