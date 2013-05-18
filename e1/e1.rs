// Project euler 1

fn e1(n: int) -> int {
	match n {
		0 => 0,
		n => { if n%3 == 0 || n%5 == 0 {
				e1(n-1) + n
			} 
			else {
				e1(n-1)
			}
		}
	}
}
fn main() {
    io::println(fmt!("%d", e1(999)))
}
