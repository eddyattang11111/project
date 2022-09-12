FROM ruimarinho/bitcoin-core:22
#USER bitcoin
RUN chown -R 999:999 /home/bitcoin/.bitcoin/

RUN cat /etc/passwd

RUN ls -ltra /home/bitcoin/.bitcoin
USER bitcoin


#CMD ["ls","-ltra","/home/bitcoin"]
ENTRYPOINT ["bitcoind"]
CMD ["-printtoconsole"]
