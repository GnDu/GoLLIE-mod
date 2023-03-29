from transformers import PreTrainedModel


def get_trainable_parameters(model: PreTrainedModel) -> (int, int, float):
    """
    Prints the number of trainable parameters in the model.
    :param model: The model to print the number of trainable parameters for.
    :return: The number of trainable parameters, the total number of parameters and the percentage of trainable parameters.
    """
    trainable_params = 0
    all_param = 0
    for _, param in model.named_parameters():
        num_params = param.numel()
        # if using DS Zero 3 and the weights are initialized empty
        if num_params == 0 and hasattr(param, "ds_numel"):
            num_params = param.ds_numel

        all_param += num_params
        if param.requires_grad:
            trainable_params += num_params

    return trainable_params, all_param, 100 * trainable_params / all_param
