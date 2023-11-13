document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('generateForm').addEventListener('change', function() {
        const controlPanel = document.getElementById('control-panel');

        if (this.checked) {
            controlPanel.innerHTML = `
                <form>
                    <div>
                        <label for="fontSize">Font size :</label>
                        <input type="number" id="fontSize" name="fontSize" min="8">
                    </div>
                    <div>
                        <label for="textColor">Text color:</label>
                        <input type="color" id="textColor" name="textColor">
                    </div>
                    <div>
                        <label for="bgColor">Background color:</label>
                        <input type="color" id="bgColor" name="bgColor">
                    </div>
                    <div>
                        <button type="button" id="applyChanges">Apply changes
                </form>
            `;

            document.getElementById('applyChanges').addEventListener('click', function() {
                let fontSize = document.getElementById('fontSize').value;
                let textColor = document.getElementById('textColor').value;
                let bgColor = document.getElementById('bgColor').value;

                document.body.style.fontSize = fontSize + 'px';
                document.body.style.color = textColor;
                document.body.style.backgroundColor = bgColor;

                let elements = document.querySelectorAll('p, a, li, h1, h2, h3, h4, h5, span, strong, em, div');

                elements.forEach((element) => {
                    element.style.fontSize = fontSize + 'px';
                    element.style.color = textColor;
                });

                let images = document.getElementsByTagName('img');
                for(let i = 0; i < images.length; i++) {
                    images[i].style.width = images[i].offsetWidth + 'px';
                    images[i].style.height = images[i].offsetHeight + 'px';
                }
            });
        } else {
            controlPanel.innerHTML = '';
        }
    });
});
