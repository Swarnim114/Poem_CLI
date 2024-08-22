# Maintainer: Your Name <your.email@example.com>
pkgname=poemcli
pkgver=0.1.0
pkgrel=1
pkgdesc="A CLI tool to fetch random poems"
arch=('any')
url="https://github.com/Swarnim114/Poem_CLI"
license=('MIT')
depends=('python' 'python-requests')
makedepends=('python-setuptools')
source=("$pkgname-$pkgver.tar.gz::https://github.com/Swarnim114/Poem_CLI/archive/v$pkgver.tar.gz")
sha256sums=('SKIP')

build() {
    cd "$pkgname-$pkgver"
    python setup.py build
}

package() {
    cd "$pkgname-$pkgver"
    python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
