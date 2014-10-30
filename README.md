rpm-python-elasticsearch
============

An RPM spec file build an RPM for [Elasticsearch-py](https://github.com/elasticsearch/elasticsearch-py)

To Build:
```
sudo yum -y install rpmdevtools && rpmdev-setuptree

PKGNAME="python-elasticsearch"
wget https://raw.github.com/mwhahaha/rpm-${PKGNAME}/master/${PKGNAME}.spec -O ~/rpmbuild/SPECS/${PKGNAME}.spec
spectool -R -g ~/rpmbuild/SPECS/${PKGNAME}.spec
wget https://raw.github.com/mwhahaha/rpm-${PKGNAME}/master/elasticsearch-py-1.2.0-urllib.patch -O ~/rpmbuild/SOURCES/elasticsearch-py-1.2.0-urllib.patch
rpmbuild -ba ~/rpmbuild/SPECS/${PKGNAME}.spec

```

### Source Attribution

Original source for spec and patch from [Matt Dainty](https://gist.github.com/bodgit/88e336f06e9924048665) ([bodgit](https://github.com/bodgit))
