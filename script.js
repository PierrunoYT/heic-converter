document.addEventListener('DOMContentLoaded', () => {
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');
    const uploadBtn = document.querySelector('.upload-btn');
    const conversionStatus = document.querySelector('.conversion-status');
    const progressBar = document.querySelector('.progress');
    const resultsSection = document.querySelector('.results-section');
    const convertedFiles = document.querySelector('.converted-files');
    const downloadAllBtn = document.querySelector('.download-all-btn');

    // Handle drag and drop events
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
            handleFiles(files);
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
        handleFiles(files);
    });

    // Handle file processing
    function handleFiles(files) {
        conversionStatus.hidden = false;
        progressBar.style.width = '0%';

        // Simulate conversion progress
        let progress = 0;
        const interval = setInterval(() => {
            progress += 5;
            progressBar.style.width = `${progress}%`;

            if (progress >= 100) {
                clearInterval(interval);
                showResults(files);
            }
        }, 100);
    }

    // Show conversion results
    function showResults(files) {
        resultsSection.hidden = false;
        convertedFiles.innerHTML = '';

        files.forEach(file => {
            const fileElement = document.createElement('div');
            fileElement.className = 'converted-file';
            fileElement.innerHTML = `
                <span>${file.name.replace('.heic', '.jpg')}</span>
                <button class="download-btn">Download</button>
            `;
            convertedFiles.appendChild(fileElement);
        });

        // Add styles for converted files
        const style = document.createElement('style');
        style.textContent = `
            .converted-file {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 1rem;
                background-color: #f8fafc;
                border-radius: 0.5rem;
            }
            .download-btn {
                background-color: var(--primary-color);
                color: white;
                border: none;
                padding: 0.5rem 1rem;
                border-radius: 0.25rem;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            .download-btn:hover {
                background-color: var(--hover-color);
            }
        `;
        document.head.appendChild(style);
    }

    // Handle download all button
    downloadAllBtn.addEventListener('click', () => {
        // In a real implementation, this would trigger the download of all converted files
        alert('Downloading all converted files...');
    });
});