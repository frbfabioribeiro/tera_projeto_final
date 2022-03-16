import bc.bancocentral as bc
from bc.bancocentral import Inflacao
from bc.bancocentral import Selic


inflacao = Inflacao()
print('%s' % inflacao.get_acumulada_tax())


selic = bc.Selic()
print(selic.get_selic_meta())