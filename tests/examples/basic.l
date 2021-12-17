import "./test.l";
import global_package.l;
import "https://global_package.com/package.l";
import my_function from "https://global_package.com/package.l";

structure example_struct {
    int x;
    int y;
    int z;

    fn __init__() {
        this.x = 0;
        this.y = 0;
        this.z = 0;
    }

    fn result() {
        let {x, y, z} = this;
        return x + y + z;
    }
}

fn dedupe(nodes : list) : list {
    let buffer : list = [];
    let holder : set = {} /* Keys are a set in a dictionary */ 

    for n in range(nodes.length) {
        let node : int = nodes[n];
        print(node);
        
        if(!holder.has(node)) {
            buffer.add(node);
            holder.add(node);
        }
    }

    return buffer;
}

fn test_function(int x, int y) {
    let my_list : list = [1, 1, 4, 1, 4, 4, 5, 4, 5, 1];
    my_list = new list(dedupe(my_list));

    let my_class : example_struct = new example_struct();
    
    my_class.x = my_list[0];
    my_class.y = my_list[1];
    my_class.z = my_list[2];

    return my_class.result();
}

let z : int = test_function(1, 3);
test_structure();