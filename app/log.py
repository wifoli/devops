"""Configuração do log da aplicação."""

import logging

LOGGER = logging.getLogger("aplicacao")
LOGGER.setLevel(logging.DEBUG)

saida_padrao = logging.StreamHandler()
arquivo = logging.FileHandler("aplicacao.log", encoding="utf-8")

formatador = logging.Formatter(
    "%(name)s | %(levelname)s | %(asctime)s | "
    "%(filename)s:%(lineno)s | %(message)s"
)

saida_padrao.setFormatter(formatador)
arquivo.setFormatter(formatador)

LOGGER.addHandler(saida_padrao)
LOGGER.addHandler(arquivo)
