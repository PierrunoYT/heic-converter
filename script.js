document.addEventListener('DOMContentLoaded', () => {
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');
    const uploadBtn = document.querySelector('.upload-btn');
    const selectedFilesSection = document.querySelector('.selected-files');
    const filesList = document.querySelector('.files-list');
    const convertBtn = document.querySelector('.convert-btn');
    const formatSelect = document.getElementById('formatSelect');
    const conversionStatus = document.querySelector('.conversion-status');
    const progressBar = document.querySelector('.progress');
    const resultsSection = document.querySelector('.results-section');
    const convertedFiles = document.querySelector('.converted-files');
    const downloadAllBtn = document.querySelector('.download-all-btn');

    let selectedFiles = [];
    let convertedFilesData = [];

    // Prevent defaults for the entire document
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        document.addEventListener(eventName, preventDefaults, false);
    });

    // Handle drag and drop events for the drop zone
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, preventDefaults);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    ['dragenter', 'dragover'].forEach(eventName => {
        dropZone.addEventListener(eventName, () => {
            dropZone.classList.add('drag-over');
        });
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, () => {
            dropZone.classList.remove('drag-over');
        });
    });

    // Handle file drop
    dropZone.addEventListener('drop', (e) => {
        const files = Array.from(e.dataTransfer.files).filter(file => 
            file.name.toLowerCase().endsWith('.heic')
        );
        if (files.length > 0) {
            addFiles(files);
        } else {
            alert('Please drop only HEIC files.');
        }
    });

    // Handle file input change
    uploadBtn.addEventListener('click', () => {
        fileInput.click();
    });

    fileInput.addEventListener('change', (e) => {
        const files = Array.from(e.target.files);
        addFiles(files);
    });

    // Add files to selection
    function addFiles(files) {
        selectedFiles = [...selectedFiles, ...files];
        updateFilesList();
        selectedFilesSection.hidden = false;
    }

    // Update the list of selected files
    function updateFilesList() {
        filesList.innerHTML = '';
        selectedFiles.forEach((file, index) => {
            const fileElement = document.createElement('div');
            fileElement.className = 'selected-file';
            fileElement.innerHTML = `
                <span>${file.name}</span>
                <button class="remove-btn" data-index="${index}">Remove</button>
            `;
            filesList.appendChild(fileElement);
        });

        // Add remove button listeners
        document.querySelectorAll('.remove-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const index = parseInt(e.target.dataset.index);
                selectedFiles.splice(index, 1);
                updateFilesList();
                if (selectedFiles.length === 0) {
                    selectedFilesSection.hidden = true;
                }
            });
        });
    }

    // Handle convert button click
    convertBtn.addEventListener('click', async () => {
        if (selectedFiles.length === 0) {
            alert('Please select files to convert');
            return;
        }

        const selectedFormat = formatSelect.value;
        conversionStatus.hidden = false;
        conversionStatus.innerHTML = 'Converting...';
        progressBar.style.width = '0%';
        convertedFilesData = [];

        try {
            for (let i = 0; i < selectedFiles.length; i++) {
                const file = selectedFiles[i];
                const progress = (i / selectedFiles.length) * 100;
                progressBar.style.width = `${progress}%`;

                const formData = new FormData();
                formData.append('file', file);
                formData.append('format', selectedFormat);

                const response = await fetch('http://localhost:5000/convert', {
                    method: 'POST',
                    body: formData
                });

                if (!response.ok) {
                    const error = await response.json();
                    throw new Error(error.error || 'Conversion failed');
                }

                const blob = await response.blob();
                convertedFilesData.push({
                    name: file.name.replace('.heic', `.${selectedFormat}`),
                    data: blob
                });
            }

            progressBar.style.width = '100%';
            showResults(selectedFiles, selectedFormat);
        } catch (error) {
            alert(`Error during conversion: ${error.message}`);
        }
    });

    // Show conversion results
    function showResults(files, format) {
        // Update conversion status to show completion
        conversionStatus.innerHTML = 'Conversion completed!';
        resultsSection.hidden = false;
        convertedFiles.innerHTML = '';

        convertedFilesData.forEach((file, index) => {
            const fileElement = document.createElement('div');
            fileElement.className = 'converted-file';
            fileElement.innerHTML = `
                <span class="file-name">${file.name}</span>
                <button class="download-btn" data-index="${index}">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                        <polyline points="7 10 12 15 17 10"></polyline>
                        <line x1="12" y1="15" x2="12" y2="3"></line>
                    </svg>
                    Download
                </button>
            `;
            convertedFiles.appendChild(fileElement);
        });

        // Add download button listeners
        document.querySelectorAll('.download-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                // Get the closest button element in case the click was on the SVG or text
                const button = e.target.closest('.download-btn');
                if (!button) return;
                
                const index = parseInt(button.dataset.index);
                const file = convertedFilesData[index];
                downloadFile(file.data, file.name);
            });
        });
    }

    // Handle download all button
    downloadAllBtn.addEventListener('click', () => {
        if (convertedFilesData.length === 0) {
            alert('No converted files to download');
            return;
        }

        convertedFilesData.forEach(file => {
            downloadFile(file.data, file.name);
        });
    });

    // Helper function to download a file
    function downloadFile(data, filename) {
        const url = URL.createObjectURL(data);
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }
});