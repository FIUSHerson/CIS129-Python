use std::io::stdin;

fn answered_yes() {

}

fn main() {
    let mut user_lives = 3;

    loop {
        let user_prompt = "Do you want to know? [Y/n]: ";
        let mut user_input = String::new();
        match stdin().read_line(&mut user_input) {
            Ok(_) => {
                user_input = user_input.trim_end().to_uppercase();

                match user_input {
                    String::from("Y") => {

                    }
                    "N" => {

                    }
                    _ => {

                    }
                }

                answered_yes();
                break;
            }
            Err(T) => {
                println!("Hmm, you have entered something invalid: {}", &T);
            }
        }
        user_lives =- 1;
    }
}
