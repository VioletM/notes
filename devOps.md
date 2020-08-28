# devOps

- **Активация окружения на конде**

    ```bash
    source activate idp
    ```

- **White theme**

    ```bash
    !jt -r
    ```

- **Dark theme**

    ```bash
    !jt -t onedork -fs 95 -tfs 11 -nfs 115 -cellw
    70% -T -N -f source
    ```

- **Jupyter run on server**

    ```bash
    jupyter notebook --no-browser --port=8889
    ssh **-**N **-**f **-**L localhost**:**YYYY**:**localhost**:**XXXX remoteuser**@**remotehost
    #open browser on http://localhost:YYYY
    ```
