FROM nginx:1.13.1

COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf
COPY start.sh /start.sh

RUN echo "deb http://archive.debian.org/debian/ stretch main contrib non-free" > /etc/apt/sources.list
RUN echo "deb http://archive.debian.org/debian/ stretch-proposed-updates main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb http://archive.debian.org/debian-security stretch/updates main contrib non-free" >> /etc/apt/sources.list
RUN apt-get update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN chmod +x /start.sh

WORKDIR /app
COPY app.py app.py
RUN echo 'FLAG{ng1nx_1n7_0v3rfl0w}' > flag_is_here.txt
RUN chmod -w flag_is_here.txt
RUN chmod +r flag_is_here.txt
RUN pip3 install flask

RUN useradd app
RUN chown app:app /app/app.py

CMD ["/start.sh"]
