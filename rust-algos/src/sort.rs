pub fn insertion_sort(arr: &mut [i32]) {

    for i in 1..arr.len() {
        let mut j = i;
        while j > 0 && arr[j] < arr[j-1] {
            arr.swap(j, j-1);
            j-=1;
        }
    }
}

pub fn merge_sort(vec: &Vec<i32>) -> Vec<i32> {
    if vec.len() < 2 {
        vec.to_vec()
    } else {
        let size = vec.len() / 2;
        let left = merge_sort(&vec[0..size].to_vec());
        let right = merge_sort(&vec[size..].to_vec());
        let merged = merge(&left, &right);

        merged
    }
}

fn merge(left: &Vec<i32>, right: &Vec<i32>) -> Vec<i32> {
    let mut i = 0;
    let mut j = 0;
    let mut merged: Vec<i32> = Vec::new();

    while i < left.len() && j < right.len() {
        if left[i] < right[j] {
            merged.push(left[i]);
            i = i + 1;
        } else {
            merged.push(right[j]);
            j = j + 1;
        }
    }

    if i < left.len() {
        while i < left.len() {
            merged.push(left[i]);
            i = i + 1;
        }
    }

    if j < right.len() {
        while j < right.len() {
            merged.push(right[j]);
            j = j + 1;
        }
    }

    merged
}



#[cfg(test)]
mod test {
    use rand::{random, Rng};

    #[test]
    fn test_insertion() {
        use super::insertion_sort;

        let small: [i32; 5] = random();
        let medium: [i32; 20] = random();
        let large: [i32; 30] = random();

        let mut cases: [Box<[i32]>; 4] = [
            Box::new(small),
            Box::new(medium),
            Box::new(large),
            Box::new([0, 0, 0, 0])
        ];

        for case in cases.iter_mut() {
            assert_eq!(case.sort(), insertion_sort(case))
        }
    }

    #[test]
    fn test_merge() {
        use super::merge_sort;

        let mut rng = rand::thread_rng();
        let small: Vec<i32> = (0..5).map(|_| rng.gen_range(0..20)).collect();
        let medium: Vec<i32> = (0..30).map(|_| rng.gen_range(-50..200)).collect(); 
        let large: Vec<i32> = (0..100).map(|_| rng.gen_range(-300..500)).collect();
         
        let mut small_sorted = small.clone();
        small_sorted.sort();
        let mut medium_sorted = medium.clone();
        medium_sorted.sort();
        let mut large_sorted = large.clone();
        large_sorted.sort();

        assert_eq!(small_sorted, merge_sort(&small));
        assert_eq!(medium_sorted, merge_sort(&medium));
        assert_eq!(large_sorted, merge_sort(&large));
    }   



}