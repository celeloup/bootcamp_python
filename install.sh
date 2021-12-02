OS=$(echo $OSTYPE | grep -i 'darwin' &>/dev/null && echo "MacOSX" || echo "Linux")

install_path="/goinfre/${whoami}"
miniconda_src="Miniconda3-latest-${OS}-x86_64.sh"

cd $install_path
curl -LO "https://repo.anaconda.com/miniconda/${miniconda_src}"
sh ${miniconda_src} -p "${install_path}/miniconda3"

cd "miniconda3/bin" && ./conda install -y jupyter numpy pandas matplotlib
