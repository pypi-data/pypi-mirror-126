Bu paket şu işe yarar şunları yapar vs vs gibi birşeyler yazması gerekiyor.


paketi sıfırdan kurup pypi.org a atmak için lattaki komutlar kullanınız


```shell
python3 setup.py sdist bdist_wheel

# paketimiz hazır şimdi paketimizi doğrulayalım
twine check dist/*

# upload için doğrulama. pypi.org domaini değl test.pypi.org sitesine ayrıca üye olmak gerekiyor.
twine upload -r testpypi dist/*
# eğer buraya publish yapabildiyseniz artık gerçek yere publish yapılabilir

twine upload dist/*
```

Kurumu yaptıktan sonra kullanım

```python
from muratin_hesap_makinasi import HesapMakinasi

hm = HesapMakinasi()

hm.topla(3,2)
# sonuc 5
```


